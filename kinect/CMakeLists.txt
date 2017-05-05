######################################################################################
# Packages needed for examples
######################################################################################

# All viewers need pthreads and GLUT.
set(THREADS_USE_PTHREADS_WIN32 true)
find_package(Threads)
find_package(OpenGL)
find_package(GLUT)


if (Threads_FOUND AND OPENGL_FOUND AND GLUT_FOUND)
  include_directories(${THREADS_PTHREADS_INCLUDE_DIR} ${OPENGL_INCLUDE_DIR} ${GLUT_INCLUDE_DIR})
  #include_directories(c_sync/)

  add_executable(hiview_test hiview.c)

  target_link_libraries(hiview_test freenect ${OPENGL_LIBRARIES} ${GLUT_LIBRARY} ${CMAKE_THREAD_LIBS_INIT} m curl)

  install(TARGETS hiview_test 
          DESTINATION bin)
endif ()

