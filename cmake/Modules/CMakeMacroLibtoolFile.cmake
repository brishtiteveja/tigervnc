macro(libtool_create_control_file _target)
  get_target_property(_target_location ${_target} LOCATION)
  get_target_property(_target_type ${_target} TYPE)

  message("-- Creating static libtool control file for target ${_target}")
  # No support for shared libraries, as TigerVNC only needs libtool config
  # files for static libraries.
  if("${_target_type}" MATCHES "^[^STATIC_LIBRARY]$")
    message(ERROR " -  trying to use libtool_create_control_file for non-static library target.")
  endif()

  #
  # Parse the target_LIB_DEPENDS variable to determine which libraries to put
  # into libtool control file as library dependencies, and handle a few corner
  # cases.
  #

  # First we need to split up any internal entries
  set(target_libs "")
  foreach(library ${${_target}_LIB_DEPENDS})
    if("${library}" MATCHES " ")
      string(REPLACE " " ";" lib_list "${library}")
      list(APPEND target_libs ${lib_list})
    else()
      list(APPEND target_libs "${library}")
    endif()
  endforeach()

  set(STATIC_MODE OFF)

  foreach(library ${target_libs})
    # Assume all entries are shared libs if platform-specific static library
    # extension is not matched.
    if("${library}" MATCHES "[^.+\\${CMAKE_STATIC_LIBRARY_SUFFIX}]$")
      if("${library}" MATCHES ".+\\${CMAKE_SHARED_LIBRARY_SUFFIX}$")
        # Shared library extension matched, so extract the path and library
        # name, then add the result to the libtool dependency libs.  This
        # will always be an absolute path, because that's what CMake uses
        # internally.
        get_filename_component(_shared_lib ${library} NAME_WE)
        get_filename_component(_shared_lib_path ${library} PATH)
        string(REPLACE "lib" "" _shared_lib ${_shared_lib})
        set(_target_dependency_libs "${_target_dependency_libs} -L${_shared_lib_path} -l${_shared_lib}")
      else()
        # No shared library extension matched.  Check whether target is a CMake
        # target.
        get_target_property(_ltp ${library} TYPE)
        if(_ltp OR ${library} STREQUAL "general")
          # Target is a CMake target, so ignore (CMake targets are static
          # libs in TigerVNC.)
        elseif(${library} STREQUAL "-Wl,-Bstatic")
          # All following libraries should be static
          set(STATIC_MODE ON)
        elseif(${library} STREQUAL "-Wl,-Bdynamic")
          # All following libraries should be dynamic
          set(STATIC_MODE OFF)
        else()
          # Normal library, so use find_library() to attempt to locate the
          # library in a system directory.

          # Need to remove -l prefix
          if (${library} MATCHES "^\\${CMAKE_LINK_LIBRARY_FLAG}")
            string(REPLACE ${CMAKE_LINK_LIBRARY_FLAG} "" library ${library})
          endif()

          if(STATIC_MODE)
            set(library ${CMAKE_STATIC_LIBRARY_PREFIX}${library}${CMAKE_STATIC_LIBRARY_SUFFIX})
          endif()

          find_library(FL ${library})
          if(FL)
            # Found library. Depending on if it's static or not we might
            # extract the path and library name, then add the
            # result to the libtool dependency libs.
            if(STATIC_MODE)
              set(_target_dependency_libs "${_target_dependency_libs} ${FL}")
            else()
              get_filename_component(_shared_lib ${FL} NAME_WE)
              get_filename_component(_shared_lib_path ${FL} PATH)
              string(REPLACE "lib" "" _shared_lib ${_shared_lib})
              set(_target_dependency_libs "${_target_dependency_libs} -L${_shared_lib_path} -l${_shared_lib}")
            endif()
          else()
            # No library found, so ignore target.
          endif()
          # Need to clear FL to get new results next loop
          unset(FL CACHE)
        endif()
      endif()
    else()
      # Detected a static library.  Check whether the library pathname is
      # absolute and, if not, use find_library() to get the abolute path.
      get_filename_component(_name ${library} NAME)
      string(REPLACE "${_name}" "" _path ${library})
      if(NOT "${_path}" STREQUAL "")
      	# Pathname is absolute, so add it to the libtool library dependencies
        # as-is.
        set(_target_dependency_libs "${_target_dependency_libs} ${library}")
      else()
        # Pathname is not absolute, so use find_library() to get the absolute
        # path.
        find_library(FL ${library})
        if(FL)
          # Absolute pathname found.  Add it.
          set(_target_dependency_libs "${_target_dependency_libs} ${FL}")
        else()
          # No absolute pathname found.  Ignore it.
        endif()
        # Need to clear FL to get new results next loop
        unset(FL CACHE)
      endif()
    endif()
  endforeach()

  # Write the libtool control file for the static library
  get_filename_component(_lname ${_target_location} NAME_WE)
  set(_laname ${CMAKE_CURRENT_BINARY_DIR}/${_lname}.la)

  file(WRITE ${_laname} "# ${_lname}.la - a libtool library file\n# Generated by ltmain.sh (GNU libtool) 2.2.6b\n")
  file(APPEND ${_laname} "dlname=''\n\n")
  file(APPEND ${_laname} "library_names=''\n\n")
  file(APPEND ${_laname} "old_library='${_lname}${CMAKE_STATIC_LIBRARY_SUFFIX}'\n\n")
  file(APPEND ${_laname} "inherited_linker_flags=''\n\n")
  file(APPEND ${_laname} "dependency_libs=' ${_target_dependency_libs}'\n\n")
  file(APPEND ${_laname} "weak_library_names=''\n\n")
  file(APPEND ${_laname} "current=\n")
  file(APPEND ${_laname} "age=\n")
  file(APPEND ${_laname} "revision=\n\n")
  file(APPEND ${_laname} "installed=no\n\n")
  file(APPEND ${_laname} "shouldnotlink=no\n\n")
  file(APPEND ${_laname} "dlopen=''\n")
  file(APPEND ${_laname} "dlpreopen=''\n\n")
<<<<<<< HEAD
  file(APPEND ${_laname} "libdir=''\n\n")
=======
  file(APPEND ${_laname} "libdir='/usr/lib'\n\n")
>>>>>>> 4c33f2ca86586bb8461526b93cba57a0a14c8baa


  # Add custom command to symlink the static library so that autotools finds
  # the library in .libs.  These are executed after the specified target build.
  add_custom_command(TARGET ${_target} POST_BUILD COMMAND 
    "${CMAKE_COMMAND}" -E make_directory "${CMAKE_CURRENT_BINARY_DIR}/.libs")
  add_custom_command(TARGET ${_target} POST_BUILD COMMAND
    "${CMAKE_COMMAND}" -E create_symlink ${_target_location} "${CMAKE_CURRENT_BINARY_DIR}/.libs/${_lname}${CMAKE_STATIC_LIBRARY_SUFFIX}")

endmacro()
