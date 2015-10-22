#define PACKAGE_NAME "tigervnc"
#define PACKAGE_VERSION "1.4.0"

#define HAVE_INET_ATON
#define HAVE_GETADDRINFO
/* #undef HAVE_GNUTLS_SET_GLOBAL_ERRNO */
#define HAVE_GNUTLS_SET_ERRNO
#define HAVE_GNUTLS_X509_CRT_PRINT
#define HAVE_GNUTLS_X509_CRT_T
#define HAVE_GNUTLS_DATUM_T
#define HAVE_GNUTLS_PK_ALGORITHM_T
#define HAVE_GNUTLS_SIGN_ALGORITHM_T
#define HAVE_FLTK_CLIPBOARD
#define HAVE_FLTK_MEDIAKEYS
#define HAVE_FLTK_FULLSCREEN
#define HAVE_FLTK_FULLSCREEN_SCREENS
#define HAVE_FLTK_CURSOR
#define HAVE_FLTK_WORK_AREA
#define HAVE_FLTK_ICONS
#define HAVE_FLTK_XHANDLERS
#define HAVE_FLTK_IM
/* #undef HAVE_ACTIVE_DESKTOP_H */
/* #undef HAVE_ACTIVE_DESKTOP_L */
/* #undef ENABLE_NLS */
#define HAVE_PAM

#define DATA_DIR "/usr/local/share"
#define LOCALE_DIR "/usr/local/share/locale"

/* MS Visual Studio 2008 and newer doesn't know ssize_t */
#if defined(HAVE_GNUTLS) && defined(WIN32) && !defined(__MINGW32__)
#include <stddef.h>
typedef size_t ssize_t;
#endif
