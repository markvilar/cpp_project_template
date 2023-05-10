from conan import ConanFile

from conan.errors import ConanInvalidConfiguration
from conan.tools.build import check_min_cppstd
from conan.tools.cmake import CMake, CMakeDeps, CMakeToolchain, cmake_layout
from conan.tools.files import copy, get, patch
from conan.tools.scm import Git, Version

from typing import Dict

required_conan_version = ">=2.0.0"

class MyProjectConanFile(ConanFile):
    name = "myproject"
    version = "0.0.1"
    license = "BSD 3-Clause"
    author = "Martin Kvisvik Larsen"
    description = "A cpptemp for C++ projects."
    url = "https://github.com/markvilar/cpp_project_template"
    homepage = "https://github.com/markvilar/cpp_project_template"

    settings = ["os", "compiler", "build_type", "arch"]
    
    options = {
        "shared" : [True, False], 
        "fPIC" : [True, False],
        "enable_warnings" : [True, False],
        "enable_examples" : [True, False],
        "enable_tests" : [True, False],
    }

    default_options = {
        "shared" : False, 
        "fPIC" : True,
        "enable_warnings" : True,
        "enable_examples" : True,
        "enable_tests" : True,
    }

    exports_sources = [
        "CMakeLists.txt", 
        "bin/*",
        "cmake/*",
        "conan/*",
        "example/*", 
        "resource/*", 
        "src/*", 
        "test/*",
    ]
    
    @property
    def _min_cppstd(self):
        return "17"

    @property
    def _compilers_minimum_version(self):
        return {
            "Visual Studio": "15.9",
            "msvc"         : "16",
            "gcc"          : "7",
            "clang"        : "8",
            "apple-clang"  : "10",
        }

    def config_options(self):
        """ Configure project options. """
        if self.settings.os == "Windows":
            del self.options.fPIC
        if self.options.shared:
            del self.options.fPIC

    def configure(self):
        """ Configures the project settings. """
        if self.options.shared:
            del self.options.fPIC

    def requirements(self):
        """ Specifies the project requirements. """
        self.requires("fmt/[>9.0.0]")

    def build_requirements(self):
        """ Specifies requirements for building the package. """
        self.tool_requires("cmake/[>=3.19]")

    def validate(self):
        """ Validates the project configuration. """
        # Check C++ standard
        if self.settings.compiler.get_safe("cppstd"):
            check_min_cppstd(self, self._min_cppstd)

        # Check compiler version
        compiler = str(self.settings.compiler)
        compiler_version = Version(self.settings.compiler.version)
        minimum_version = Version(
            self._compilers_minimum_version.get(compiler)
        )
        if minimum_version and minimum_version > compiler_version:
            raise ConanInvalidConfiguration(
                f"{self.ref} requires C++{self._min_cppstd}, which your "
                "compiler does not support.",
            )

    def layout(self):
        """ Defines the project layout. """
        self.folders.root = "."
        self.folders.source = "."
        self.folders.build = "build"
        cmake_layout(self)

    def source(self):
        """ Retrieves and prepares source code for the package. """
        # NOTE: For reference
        # git = tools.Git(folder=self.folders.source)
        # git.clone("https://github.com/myuser/mypackage.git")
        # git.checkout("v1.0")
        pass

    def _get_cmake_variables(self) -> Dict:
        """ Internal methods to get CMake variables based on options. """
        return {
            "PROJECT_BUILD_SHARED" : 
                "ON" if self.options.shared else "OFF",
            "PROJECT_WARNINGS_ENABLED" : 
                "ON" if self.options.enable_warnings else "OFF",
            "PROJECT_EXAMPLES_ENABLED" :
                "ON" if self.options.enable_examples else "OFF",
            "PROJECT_TESTS_ENABLED" :
                "ON" if self.options.enable_tests else "OFF",
        }

    def generate(self):
        """ Generates files necessary for build the package. """
        # Create dependency graph
        deps = CMakeDeps(self)
        deps.generate()

        # Set up toolchain
        tc = CMakeToolchain(self)

        # Add variables to toolchain
        variables = self._get_cmake_variables()
        for name, value in variables.items():
            tc.variables[name] = value
        
        # NOTE: For reference
        # tc.preprocessor_definitions
        # tc.cache_variables
        # tc.variables

        tc.generate()

    def build(self):
        """ Builds the library. """
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        """ Packages the library. """
        copy(self, pattern="LICENSE*", dst="licenses", src=self.source_folder)
        cmake = CMake(self)
        variables = self._get_cmake_variables()
        cmake.configure(variables=variables)
        cmake.install()

    def package_info(self):
        """ Configures the package information. """
        # Set up component and properties
        component = self.cpp_info.components["libcpptemp"]
        component.set_property("cmake_file_name", "cpptemp")
        component.set_property("cmake_target_name", "cpptemp::cpptemp")
        component.set_property("pkg_config_name", "cpptemp-config.cmake")

        # Component attributes
        component.libs = ["myproject::cpptemp"]
        component.resdirs= ["resource"]
        component.requires = ["fmt::fmt"]

        # Architecture definitions
        if self.settings.os == "Windows":
            self.cpp_info.components["cpptemp"].defines \
                .append("CPPTEMP_PLATFORM_WINDOWS")
        elif self.settings.os == "Linux":
            self.cpp_info.components["cpptemp"].defines \
                .append("CPPTEMP_PLATFORM_LINUX")

        # Build type definitions
        if self.settings.build_type == "Debug":
            self.cpp_info.components["cpptemp"].defines \
                .append("CPPTEMP_DEBUG_DEFINITION")
        elif self.settings.build_type == "Release":
            self.cpp_info.components["cpptemp"].defines \
                .append("CPPTEMP_RELEASE_DEFINITION")

    def export(self):
        """ Responsible for capturing the coordinates of the current URL and 
        commit. """
        # TODO: Implement
        pass
