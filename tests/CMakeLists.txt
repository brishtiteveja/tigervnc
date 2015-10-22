include_directories(${CMAKE_SOURCE_DIR}/common)

add_library(test_util STATIC util.cxx)

add_executable(convperf convperf.cxx)
target_link_libraries(convperf test_util rfb)

add_executable(conv conv.cxx)
target_link_libraries(conv rfb)
<<<<<<< HEAD
=======

add_executable(decperf decperf.cxx)
target_link_libraries(decperf test_util rfb)

add_executable(encperf encperf.cxx)
target_link_libraries(encperf test_util rfb)
>>>>>>> 4c33f2ca86586bb8461526b93cba57a0a14c8baa
