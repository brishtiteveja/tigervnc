# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.2

#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:

# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list

# Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:
.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/local/Cellar/cmake/3.2.2/bin/cmake

# The command to remove a file.
RM = /usr/local/Cellar/cmake/3.2.2/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /Library/Caches/Homebrew/tigervnc-1.4.0

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /Library/Caches/Homebrew/tigervnc-1.4.0

# Include any dependencies generated for this target.
include tests/CMakeFiles/convperf.dir/depend.make

# Include the progress variables for this target.
include tests/CMakeFiles/convperf.dir/progress.make

# Include the compile flags for this target's objects.
include tests/CMakeFiles/convperf.dir/flags.make

tests/CMakeFiles/convperf.dir/convperf.cxx.o: tests/CMakeFiles/convperf.dir/flags.make
tests/CMakeFiles/convperf.dir/convperf.cxx.o: tests/convperf.cxx
	$(CMAKE_COMMAND) -E cmake_progress_report /Library/Caches/Homebrew/tigervnc-1.4.0/CMakeFiles $(CMAKE_PROGRESS_1)
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Building CXX object tests/CMakeFiles/convperf.dir/convperf.cxx.o"
	cd /Library/Caches/Homebrew/tigervnc-1.4.0/tests && /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/c++   $(CXX_DEFINES) $(CXX_FLAGS) -o CMakeFiles/convperf.dir/convperf.cxx.o -c /Library/Caches/Homebrew/tigervnc-1.4.0/tests/convperf.cxx

tests/CMakeFiles/convperf.dir/convperf.cxx.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/convperf.dir/convperf.cxx.i"
	cd /Library/Caches/Homebrew/tigervnc-1.4.0/tests && /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/c++  $(CXX_DEFINES) $(CXX_FLAGS) -E /Library/Caches/Homebrew/tigervnc-1.4.0/tests/convperf.cxx > CMakeFiles/convperf.dir/convperf.cxx.i

tests/CMakeFiles/convperf.dir/convperf.cxx.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/convperf.dir/convperf.cxx.s"
	cd /Library/Caches/Homebrew/tigervnc-1.4.0/tests && /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/c++  $(CXX_DEFINES) $(CXX_FLAGS) -S /Library/Caches/Homebrew/tigervnc-1.4.0/tests/convperf.cxx -o CMakeFiles/convperf.dir/convperf.cxx.s

tests/CMakeFiles/convperf.dir/convperf.cxx.o.requires:
.PHONY : tests/CMakeFiles/convperf.dir/convperf.cxx.o.requires

tests/CMakeFiles/convperf.dir/convperf.cxx.o.provides: tests/CMakeFiles/convperf.dir/convperf.cxx.o.requires
	$(MAKE) -f tests/CMakeFiles/convperf.dir/build.make tests/CMakeFiles/convperf.dir/convperf.cxx.o.provides.build
.PHONY : tests/CMakeFiles/convperf.dir/convperf.cxx.o.provides

tests/CMakeFiles/convperf.dir/convperf.cxx.o.provides.build: tests/CMakeFiles/convperf.dir/convperf.cxx.o

# Object files for target convperf
convperf_OBJECTS = \
"CMakeFiles/convperf.dir/convperf.cxx.o"

# External object files for target convperf
convperf_EXTERNAL_OBJECTS =

tests/convperf: tests/CMakeFiles/convperf.dir/convperf.cxx.o
tests/convperf: tests/CMakeFiles/convperf.dir/build.make
tests/convperf: tests/libtest_util.a
tests/convperf: common/rfb/librfb.a
tests/convperf: /usr/local/lib/libjpeg.dylib
tests/convperf: common/rdr/librdr.a
tests/convperf: common/os/libos.a
tests/convperf: /usr/lib/libz.dylib
tests/convperf: /usr/local/Cellar/gnutls/3.3.15/lib/libgnutls.dylib
tests/convperf: tests/CMakeFiles/convperf.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --red --bold "Linking CXX executable convperf"
	cd /Library/Caches/Homebrew/tigervnc-1.4.0/tests && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/convperf.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
tests/CMakeFiles/convperf.dir/build: tests/convperf
.PHONY : tests/CMakeFiles/convperf.dir/build

tests/CMakeFiles/convperf.dir/requires: tests/CMakeFiles/convperf.dir/convperf.cxx.o.requires
.PHONY : tests/CMakeFiles/convperf.dir/requires

tests/CMakeFiles/convperf.dir/clean:
	cd /Library/Caches/Homebrew/tigervnc-1.4.0/tests && $(CMAKE_COMMAND) -P CMakeFiles/convperf.dir/cmake_clean.cmake
.PHONY : tests/CMakeFiles/convperf.dir/clean

tests/CMakeFiles/convperf.dir/depend:
	cd /Library/Caches/Homebrew/tigervnc-1.4.0 && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /Library/Caches/Homebrew/tigervnc-1.4.0 /Library/Caches/Homebrew/tigervnc-1.4.0/tests /Library/Caches/Homebrew/tigervnc-1.4.0 /Library/Caches/Homebrew/tigervnc-1.4.0/tests /Library/Caches/Homebrew/tigervnc-1.4.0/tests/CMakeFiles/convperf.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : tests/CMakeFiles/convperf.dir/depend

