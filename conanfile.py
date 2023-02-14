from conans import ConanFile, CMake, tools

required_conan_version = ">=1.58.0"

class MyProjectConanFile(ConanFile):
    name = "myproject"
    version = "0.0.1"
    license = "BSD 3-Clause"
    author = "Martin Kvisvik Larsen"
    description = "A template for C++ projects."
    url = "https://github.com/markvilar/cpp_project_template"
    homepage = "https://github.com/markvilar/cpp_project_template"

    settings = ["os", "compiler", "build_type", "arch"]
    
    options = {
        "shared" : [True, False], 
        "fPIC" : [True, False]
    }
    
    default_options = {
        "shared" : False, 
        "fPIC" : True
    }

    exports_sources = [
        "CMakeLists.txt", 
        "cmake/*",
        "examples/*", 
        "src/*", 
        "resources/*", 
        "test/*",
        "vendor/*"
    ]
    
    generators = ["cmake_find_package", "cmake_find_package_multi"]

    @property
    def _source_subfolder(self):
        return "source_subfolder"

    @property
    def _build_subfolder(self):
        return "build_subfolder"

    def config_options(self):
        if self.settings.os == "Windows":
            del self.options.fPIC

    def configure(self):
        """ Configures the project settings. """
        if self.options.shared:
            del self.options.fPIC
        self.options["fmt"].header_only = True

    def requirements(self):
        """ Specifies the project requirements. """
        self.requires("fmt/[>9.0.0]")

    def validate(self):
        """ Validates the project configuration. """
        if self.settings.compiler == "clang":
            if tools.Version(self.settings.compiler.version) < "8":
                raise ConanInvalidConfiguration("Invalid clang compiler \
                    version.")
        if self.settings.compiler == "gcc":
            if tools.Version(self.settings.compiler.version) < "7":
                raise ConanInvalidConfiguration("Invalid gcc compiler \
                    version.")
        if self.settings.compiler == "Visual Studio":
            if tools.Version(self.settings.compiler.version) < "16":
                raise ConanInvalidConfiguration("Invalid Visual Studio \
                    compiler version.")

    def _configure_cmake(self):
        """ Internal - Configures CMake"""
        cmake = CMake(self)
        cmake.definitions["PROJECT_BUILD_SHARED"] = self.options["shared"]
        cmake.definitions["PROJECT_CONAN_ENABLED"] = True
        cmake.definitions["PROJECT_WARNINGS_ENABLED"] = True
        cmake.definitions["PROJECT_EXAMPLES_ENABLED"] = True
        cmake.definitions["PROJECT_TESTS_ENABLED"] = True
        cmake.configure(build_folder=self._build_subfolder)        
        return cmake

    def build(self):
        """ Builds the project. """
        cmake = self._configure_cmake()
        cmake.build()

    def package(self):
        """ Packages the project. """
        self.copy("LICENSE*", dst="licenses", src=self._source_subfolder)
        cmake = self._configure_cmake()
        cmake.install()

    def package_info(self):
        """ Configures the package information. """
        self.cpp_info.components["mylib"].libs = ["fmt::fmt"]
        self.cpp_info.components["mylib"].resdirs= ["resource"]

        if self.settings.build_type == "Debug":
            self.cpp_info.components["mylib"].defines \
                .append("MYLIB_DEBUG_DEFINITION")
        elif self.settings.build_type == "Release":
            self.cpp_info.components["mylib"].defines \
                .append("MYLIB_RELEASE_DEFINITION")
