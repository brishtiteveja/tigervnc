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
include common/network/CMakeFiles/network.dir/depend.make

# Include the progress variables for this target.
include common/network/CMakeFiles/network.dir/progress.make

# Include the compile flags for this target's objects.
include common/network/CMakeFiles/network.dir/flags.make

common/network/CMakeFiles/network.dir/TcpSocket.cxx.o: common/network/CMakeFiles/network.dir/flags.make
common/network/CMakeFiles/network.dir/TcpSocket.cxx.o: common/network/TcpSocket.cxx
	$(CMAKE_COMMAND) -E cmake_progress_report /Library/Caches/Homebrew/tigervnc-1.4.0/CMakeFiles $(CMAKE_PROGRESS_1)
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Building CXX object common/network/CMakeFiles/network.dir/TcpSocket.cxx.o"
	cd /Library/Caches/Homebrew/tigervnc-1.4.0/common/network && /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/c++   $(CXX_DEFINES) $(CXX_FLAGS) -o CMakeFiles/network.dir/TcpSocket.cxx.o -c /Library/Caches/Homebrew/tigervnc-1.4.0/common/network/TcpSocket.cxx

common/network/CMakeFiles/network.dir/TcpSocket.cxx.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/network.dir/TcpSocket.cxx.i"
	cd /Library/Caches/Homebrew/tigervnc-1.4.0/common/network && /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/c++  $(CXX_DEFINES) $(CXX_FLAGS) -E /Library/Caches/Homebrew/tigervnc-1.4.0/common/network/TcpSocket.cxx > CMakeFiles/network.dir/TcpSocket.cxx.i

common/network/CMakeFiles/network.dir/TcpSocket.cxx.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/network.dir/TcpSocket.cxx.s"
	cd /Library/Caches/Homebrew/tigervnc-1.4.0/common/network && /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/c++  $(CXX_DEFINES) $(CXX_FLAGS) -S /Library/Caches/Homebrew/tigervnc-1.4.0/common/network/TcpSocket.cxx -o CMakeFiles/network.dir/TcpSocket.cxx.s

common/network/CMakeFiles/network.dir/TcpSocket.cxx.o.requires:
.PHONY : common/network/CMakeFiles/network.dir/TcpSocket.cxx.o.requires

common/network/CMakeFiles/network.dir/TcpSocket.cxx.o.provides: common/network/CMakeFiles/network.dir/TcpSocket.cxx.o.requires
	$(MAKE) -f common/network/CMakeFiles/network.dir/build.make common/network/CMakeFiles/network.dir/TcpSocket.cxx.o.provides.build
.PHONY : common/network/CMakeFiles/network.dir/TcpSocket.cxx.o.provides

common/network/CMakeFiles/network.dir/TcpSocket.cxx.o.provides.build: common/network/CMakeFiles/network.dir/TcpSocket.cxx.o

# Object files for target network
network_OBJECTS = \
"CMakeFiles/network.dir/TcpSocket.cxx.o"

# External object files for target network
network_EXTERNAL_OBJECTS =

common/network/libnetwork.a: common/network/CMakeFiles/network.dir/TcpSocket.cxx.o
common/network/libnetwork.a: common/network/CMakeFiles/network.dir/build.make
common/network/libnetwork.a: common/network/CMakeFiles/network.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --red --bold "Linking CXX static library libnetwork.a"
	cd /Library/Caches/Homebrew/tigervnc-1.4.0/common/network && $(CMAKE_COMMAND) -P CMakeFiles/network.dir/cmake_clean_target.cmake
	cd /Library/Caches/Homebrew/tigervnc-1.4.0/common/network && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/network.dir/link.txt --verbose=$(VERBOSE)
	cd /Library/Caches/Homebrew/tigervnc-1.4.0/common/network && /usr/local/Cellar/cmake/3.2.2/bin/cmake -E make_directory /Library/Caches/Homebrew/tigervnc-1.4.0/common/network/.libs
	cd /Library/Caches/Homebrew/tigervnc-1.4.0/common/network && /usr/local/Cellar/cmake/3.2.2/bin/cmake -E create_symlink /Library/Caches/Homebrew/tigervnc-1.4.0/common/network/libnetwork.a /Library/Caches/Homebrew/tigervnc-1.4.0/common/network/.libs/libnetwork.a

# Rule to build all files generated by this target.
common/network/CMakeFiles/network.dir/build: common/network/libnetwork.a
.PHONY : common/network/CMakeFiles/network.dir/build

common/network/CMakeFiles/network.dir/requires: common/network/CMakeFiles/network.dir/TcpSocket.cxx.o.requires
.PHONY : common/network/CMakeFiles/network.dir/requires

common/network/CMakeFiles/network.dir/clean:
	cd /Library/Caches/Homebrew/tigervnc-1.4.0/common/network && $(CMAKE_COMMAND) -P CMakeFiles/network.dir/cmake_clean.cmake
.PHONY : common/network/CMakeFiles/network.dir/clean

common/network/CMakeFiles/network.dir/depend:
	cd /Library/Caches/Homebrew/tigervnc-1.4.0 && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /Library/Caches/Homebrew/tigervnc-1.4.0 /Library/Caches/Homebrew/tigervnc-1.4.0/common/network /Library/Caches/Homebrew/tigervnc-1.4.0 /Library/Caches/Homebrew/tigervnc-1.4.0/common/network /Library/Caches/Homebrew/tigervnc-1.4.0/common/network/CMakeFiles/network.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : common/network/CMakeFiles/network.dir/depend

