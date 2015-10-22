include_directories(${CMAKE_SOURCE_DIR}/common)

add_library(os STATIC
  w32tiger.c
<<<<<<< HEAD
  os.cxx
  tls.cxx)
=======
  os.cxx)
>>>>>>> 4c33f2ca86586bb8461526b93cba57a0a14c8baa

if(UNIX)
  libtool_create_control_file(os)
endif()
