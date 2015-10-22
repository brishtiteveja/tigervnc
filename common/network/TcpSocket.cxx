/* Copyright (C) 2002-2005 RealVNC Ltd.  All Rights Reserved.
 * 
 * This is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 2 of the License, or
 * (at your option) any later version.
 * 
 * This software is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 * 
 * You should have received a copy of the GNU General Public License
 * along with this software; if not, write to the Free Software
 * Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307,
 * USA.
 */

#ifdef HAVE_CONFIG_H
#include <config.h>
#endif

#ifdef WIN32
//#include <io.h>
#include <winsock2.h>
#include <ws2tcpip.h>
#define errorNumber WSAGetLastError()
#else
#define errorNumber errno
#define closesocket close
#include <sys/types.h>
#include <sys/socket.h>
#include <arpa/inet.h>
<<<<<<< HEAD
#include <netinet/in.h>
#include <netinet/tcp.h>
#include <netdb.h>
#include <unistd.h>
=======
#include <netinet/tcp.h>
#include <netdb.h>
>>>>>>> 4c33f2ca86586bb8461526b93cba57a0a14c8baa
#include <errno.h>
#include <string.h>
#include <signal.h>
#include <fcntl.h>
#endif

#include <stdlib.h>
<<<<<<< HEAD
#include <network/TcpSocket.h>
#include <rfb/util.h>
#include <rfb/LogWriter.h>
=======
#include <unistd.h>
#include <network/TcpSocket.h>
#include <rfb/util.h>
#include <rfb/LogWriter.h>
#include <rfb/Configuration.h>

#ifdef WIN32
#include <os/winerrno.h>
#endif
>>>>>>> 4c33f2ca86586bb8461526b93cba57a0a14c8baa

#ifndef INADDR_NONE
#define INADDR_NONE ((unsigned long)-1)
#endif
#ifndef INADDR_LOOPBACK
#define INADDR_LOOPBACK ((unsigned long)0x7F000001)
#endif

<<<<<<< HEAD
#if defined(HAVE_GETADDRINFO) && !defined(IN6_ARE_ADDR_EQUAL)
=======
#ifndef IN6_ARE_ADDR_EQUAL
>>>>>>> 4c33f2ca86586bb8461526b93cba57a0a14c8baa
#define IN6_ARE_ADDR_EQUAL(a,b) \
  (memcmp ((const void*)(a), (const void*)(b), sizeof (struct in6_addr)) == 0)
#endif

<<<<<<< HEAD
using namespace network;
using namespace rdr;

typedef struct vnc_sockaddr {
	union {
		sockaddr	sa;
		sockaddr_in	sin;
#ifdef HAVE_GETADDRINFO
		sockaddr_in6	sin6;
#endif
	} u;
} vnc_sockaddr_t;

static rfb::LogWriter vlog("TcpSocket");

=======
// Missing on older Windows and OS X
#ifndef AI_NUMERICSERV
#define AI_NUMERICSERV 0
#endif

using namespace network;
using namespace rdr;

static rfb::LogWriter vlog("TcpSocket");

static rfb::BoolParameter UseIPv4("UseIPv4", "Use IPv4 for incoming and outgoing connections.", true);
static rfb::BoolParameter UseIPv6("UseIPv6", "Use IPv6 for incoming and outgoing connections.", true);

>>>>>>> 4c33f2ca86586bb8461526b93cba57a0a14c8baa
/* Tunnelling support. */
int network::findFreeTcpPort (void)
{
  int sock;
  struct sockaddr_in addr;
  memset(&addr, 0, sizeof(addr));
  addr.sin_family = AF_INET;
  addr.sin_addr.s_addr = INADDR_ANY;

  if ((sock = socket (AF_INET, SOCK_STREAM, 0)) < 0)
    throw SocketException ("unable to create socket", errorNumber);

  addr.sin_port = 0;
  if (bind (sock, (struct sockaddr *)&addr, sizeof (addr)) < 0)
    throw SocketException ("unable to find free port", errorNumber);

  socklen_t n = sizeof(addr);
  if (getsockname (sock, (struct sockaddr *)&addr, &n) < 0)
    throw SocketException ("unable to get port number", errorNumber);

  closesocket (sock);
  return ntohs(addr.sin_port);
}


// -=- Socket initialisation
static bool socketsInitialised = false;
static void initSockets() {
  if (socketsInitialised)
    return;
#ifdef WIN32
  WORD requiredVersion = MAKEWORD(2,0);
  WSADATA initResult;
  
  if (WSAStartup(requiredVersion, &initResult) != 0)
    throw SocketException("unable to initialise Winsock2", errorNumber);
#else
  signal(SIGPIPE, SIG_IGN);
#endif
  socketsInitialised = true;
}


<<<<<<< HEAD
=======
// -=- Socket duplication help for Windows
static int dupsocket(int fd)
{
#ifdef WIN32
  int ret;
  WSAPROTOCOL_INFO info;
  ret = WSADuplicateSocket(fd, GetCurrentProcessId(), &info);
  if (ret != 0)
    throw SocketException("unable to duplicate socket", errorNumber);
  return WSASocket(info.iAddressFamily, info.iSocketType, info.iProtocol,
                   &info, 0, 0);
#else
  return dup(fd);
#endif
}


>>>>>>> 4c33f2ca86586bb8461526b93cba57a0a14c8baa
// -=- TcpSocket

TcpSocket::TcpSocket(int sock, bool close)
  : Socket(new FdInStream(sock), new FdOutStream(sock), true), closeFd(close)
{
}

TcpSocket::TcpSocket(const char *host, int port)
  : closeFd(true)
{
  int sock, err, result, family;
  vnc_sockaddr_t sa;
  socklen_t salen;
<<<<<<< HEAD
#ifdef HAVE_GETADDRINFO
  struct addrinfo *ai, *current, hints;
#endif
=======
  struct addrinfo *ai, *current, hints;
>>>>>>> 4c33f2ca86586bb8461526b93cba57a0a14c8baa

  // - Create a socket
  initSockets();

<<<<<<< HEAD
#ifdef HAVE_GETADDRINFO
=======
>>>>>>> 4c33f2ca86586bb8461526b93cba57a0a14c8baa
  memset(&hints, 0, sizeof(struct addrinfo));
  hints.ai_family = AF_UNSPEC;
  hints.ai_socktype = SOCK_STREAM;
  hints.ai_canonname = NULL;
  hints.ai_addr = NULL;
  hints.ai_next = NULL;

  if ((result = getaddrinfo(host, NULL, &hints, &ai)) != 0) {
    throw Exception("unable to resolve host by name: %s",
<<<<<<< HEAD
		    gai_strerror(result));
  }

  for (current = ai; current != NULL; current = current->ai_next) {
    family = current->ai_family;
    if (family != AF_INET && family != AF_INET6)
      continue;
=======
                    gai_strerror(result));
  }

  // This logic is too complex for the compiler to determine if
  // sock is properly assigned or not.
  sock = -1;

  for (current = ai; current != NULL; current = current->ai_next) {
    family = current->ai_family;

    switch (family) {
    case AF_INET:
      if (!UseIPv4)
        continue;
      break;
    case AF_INET6:
      if (!UseIPv6)
        continue;
      break;
    default:
      continue;
    }
>>>>>>> 4c33f2ca86586bb8461526b93cba57a0a14c8baa

    salen = current->ai_addrlen;
    memcpy(&sa, current->ai_addr, salen);

    if (family == AF_INET)
      sa.u.sin.sin_port = htons(port);
    else
      sa.u.sin6.sin6_port = htons(port);

<<<<<<< HEAD
#else /* HAVE_GETADDRINFO */
    family = AF_INET;
    salen = sizeof(struct sockaddr_in);

    /* Try processing the host as an IP address */
    memset(&sa, 0, sizeof(sa));
    sa.u.sin.sin_family = AF_INET;
    sa.u.sin.sin_addr.s_addr = inet_addr((char *)host);
    sa.u.sin.sin_port = htons(port);
    if ((int)sa.u.sin.sin_addr.s_addr == -1) {
      /* Host was not an IP address - try resolving as DNS name */
      struct hostent *hostinfo;
      hostinfo = gethostbyname((char *)host);
      if (hostinfo && hostinfo->h_addr) {
        sa.u.sin.sin_addr.s_addr = ((struct in_addr *)hostinfo->h_addr)->s_addr;
      } else {
        err = errorNumber;
        throw SocketException("unable to resolve host by name", err);
      }
    }
#endif /* HAVE_GETADDRINFO */

    sock = socket (family, SOCK_STREAM, 0);
    if (sock == -1) {
      err = errorNumber;
#ifdef HAVE_GETADDRINFO
      freeaddrinfo(ai);
#endif /* HAVE_GETADDRINFO */
=======
    sock = socket (family, SOCK_STREAM, 0);
    if (sock == -1) {
      err = errorNumber;
      freeaddrinfo(ai);
>>>>>>> 4c33f2ca86586bb8461526b93cba57a0a14c8baa
      throw SocketException("unable to create socket", err);
    }

  /* Attempt to connect to the remote host */
    while ((result = connect(sock, &sa.u.sa, salen)) == -1) {
      err = errorNumber;
#ifndef WIN32
      if (err == EINTR)
<<<<<<< HEAD
	continue;
=======
        continue;
>>>>>>> 4c33f2ca86586bb8461526b93cba57a0a14c8baa
#endif
      closesocket(sock);
      break;
    }

<<<<<<< HEAD
#ifdef HAVE_GETADDRINFO
=======
>>>>>>> 4c33f2ca86586bb8461526b93cba57a0a14c8baa
    if (result == 0)
      break;
  }

  freeaddrinfo(ai);
<<<<<<< HEAD
#endif /* HAVE_GETADDRINFO */
=======

  if (current == NULL)
    throw Exception("No useful address for host");
>>>>>>> 4c33f2ca86586bb8461526b93cba57a0a14c8baa

  if (result == -1)
    throw SocketException("unable connect to socket", err);

#ifndef WIN32
  // - By default, close the socket on exec()
  fcntl(sock, F_SETFD, FD_CLOEXEC);
#endif

  // Disable Nagle's algorithm, to reduce latency
  enableNagles(sock, false);

  // Create the input and output streams
  instream = new FdInStream(sock);
  outstream = new FdOutStream(sock);
  ownStreams = true;
}

TcpSocket::~TcpSocket() {
  if (closeFd)
    closesocket(getFd());
}

int TcpSocket::getMyPort() {
  return getSockPort(getFd());
}

char* TcpSocket::getPeerAddress() {
<<<<<<< HEAD
  struct sockaddr_in  info;
  struct in_addr    addr;
  socklen_t info_size = sizeof(info);

  getpeername(getFd(), (struct sockaddr *)&info, &info_size);
  memcpy(&addr, &info.sin_addr, sizeof(addr));

  char* name = inet_ntoa(addr);
  if (name) {
    return rfb::strDup(name);
  } else {
    return rfb::strDup("");
  }
}

int TcpSocket::getPeerPort() {
  struct sockaddr_in  info;
  socklen_t info_size = sizeof(info);

  getpeername(getFd(), (struct sockaddr *)&info, &info_size);
  return ntohs(info.sin_port);
=======
  vnc_sockaddr_t sa;
  socklen_t sa_size = sizeof(sa);

  if (getpeername(getFd(), &sa.u.sa, &sa_size) != 0) {
    vlog.error("unable to get peer name for socket");
    return rfb::strDup("");
  }

  if (sa.u.sa.sa_family == AF_INET6) {
    char buffer[INET6_ADDRSTRLEN + 2];
    int ret;

    buffer[0] = '[';

    ret = getnameinfo(&sa.u.sa, sizeof(sa.u.sin6),
                      buffer + 1, sizeof(buffer) - 2, NULL, 0,
                      NI_NUMERICHOST);
    if (ret != 0) {
      vlog.error("unable to convert peer name to a string");
      return rfb::strDup("");
    }

    strcat(buffer, "]");

    return rfb::strDup(buffer);
  }

  if (sa.u.sa.sa_family == AF_INET) {
    char *name;

    name = inet_ntoa(sa.u.sin.sin_addr);
    if (name == NULL) {
      vlog.error("unable to convert peer name to a string");
      return rfb::strDup("");
    }

    return rfb::strDup(name);
  }

  vlog.error("unknown address family for socket");
  return rfb::strDup("");
}

int TcpSocket::getPeerPort() {
  vnc_sockaddr_t sa;
  socklen_t sa_size = sizeof(sa);

  getpeername(getFd(), &sa.u.sa, &sa_size);

  switch (sa.u.sa.sa_family) {
  case AF_INET6:
    return ntohs(sa.u.sin6.sin6_port);
  case AF_INET:
    return ntohs(sa.u.sin.sin_port);
  default:
    return 0;
  }
>>>>>>> 4c33f2ca86586bb8461526b93cba57a0a14c8baa
}

char* TcpSocket::getPeerEndpoint() {
  rfb::CharArray address; address.buf = getPeerAddress();
  int port = getPeerPort();

  int buflen = strlen(address.buf) + 32;
  char* buffer = new char[buflen];
  sprintf(buffer, "%s::%d", address.buf, port);
  return buffer;
}

bool TcpSocket::sameMachine() {
  vnc_sockaddr_t peeraddr, myaddr;
  socklen_t addrlen;

  addrlen = sizeof(peeraddr);
  if (getpeername(getFd(), &peeraddr.u.sa, &addrlen) < 0)
      throw SocketException ("unable to get peer address", errorNumber);

  addrlen = sizeof(myaddr); /* need to reset, since getpeername overwrote */
  if (getsockname(getFd(), &myaddr.u.sa, &addrlen) < 0)
      throw SocketException ("unable to get my address", errorNumber);

  if (peeraddr.u.sa.sa_family != myaddr.u.sa.sa_family)
      return false;

<<<<<<< HEAD
#ifdef HAVE_GETADDRINFO
  if (peeraddr.u.sa.sa_family == AF_INET6)
      return IN6_ARE_ADDR_EQUAL(&peeraddr.u.sin6.sin6_addr,
				&myaddr.u.sin6.sin6_addr);
#endif

  return (peeraddr.u.sin.sin_addr.s_addr == myaddr.u.sin.sin_addr.s_addr);
=======
  if (peeraddr.u.sa.sa_family == AF_INET6)
      return IN6_ARE_ADDR_EQUAL(&peeraddr.u.sin6.sin6_addr,
                                &myaddr.u.sin6.sin6_addr);
  if (peeraddr.u.sa.sa_family == AF_INET)
    return (peeraddr.u.sin.sin_addr.s_addr == myaddr.u.sin.sin_addr.s_addr);

  // No idea what this is. Assume we're on different machines.
  return false;
>>>>>>> 4c33f2ca86586bb8461526b93cba57a0a14c8baa
}

void TcpSocket::shutdown()
{
  Socket::shutdown();
  ::shutdown(getFd(), 2);
}

bool TcpSocket::enableNagles(int sock, bool enable) {
  int one = enable ? 0 : 1;
  if (setsockopt(sock, IPPROTO_TCP, TCP_NODELAY,
<<<<<<< HEAD
		 (char *)&one, sizeof(one)) < 0) {
=======
                 (char *)&one, sizeof(one)) < 0) {
>>>>>>> 4c33f2ca86586bb8461526b93cba57a0a14c8baa
    int e = errorNumber;
    vlog.error("unable to setsockopt TCP_NODELAY: %d", e);
    return false;
  }
  return true;
}

bool TcpSocket::cork(int sock, bool enable) {
#ifndef TCP_CORK
  return false;
#else
  int one = enable ? 1 : 0;
  if (setsockopt(sock, IPPROTO_TCP, TCP_CORK, (char *)&one, sizeof(one)) < 0)
    return false;
  return true;
#endif
}

bool TcpSocket::isSocket(int sock)
{
<<<<<<< HEAD
  struct sockaddr_in info;
  socklen_t info_size = sizeof(info);
  return getsockname(sock, (struct sockaddr *)&info, &info_size) >= 0;
=======
  vnc_sockaddr_t sa;
  socklen_t sa_size = sizeof(sa);
  return getsockname(sock, &sa.u.sa, &sa_size) >= 0;
>>>>>>> 4c33f2ca86586bb8461526b93cba57a0a14c8baa
}

bool TcpSocket::isConnected(int sock)
{
<<<<<<< HEAD
  struct sockaddr_in info;
  socklen_t info_size = sizeof(info);
  return getpeername(sock, (struct sockaddr *)&info, &info_size) >= 0;
=======
  vnc_sockaddr_t sa;
  socklen_t sa_size = sizeof(sa);
  return getpeername(sock, &sa.u.sa, &sa_size) >= 0;
>>>>>>> 4c33f2ca86586bb8461526b93cba57a0a14c8baa
}

int TcpSocket::getSockPort(int sock)
{
<<<<<<< HEAD
  struct sockaddr_in info;
  socklen_t info_size = sizeof(info);
  if (getsockname(sock, (struct sockaddr *)&info, &info_size) < 0)
    return 0;
  return ntohs(info.sin_port);
}


TcpListener::TcpListener(const char *listenaddr, int port, bool localhostOnly,
			 int sock, bool close_) : closeFd(close_)
{
  if (sock != -1) {
    fd = sock;
    return;
  }

  initSockets();
  if ((fd = socket(AF_INET, SOCK_STREAM, 0)) < 0)
    throw SocketException("unable to create listening socket", errorNumber);

#ifndef WIN32
  // - By default, close the socket on exec()
  fcntl(fd, F_SETFD, FD_CLOEXEC);

  int one = 1;
  if (setsockopt(fd, SOL_SOCKET, SO_REUSEADDR,
		 (char *)&one, sizeof(one)) < 0) {
    int e = errorNumber;
    closesocket(fd);
=======
  vnc_sockaddr_t sa;
  socklen_t sa_size = sizeof(sa);
  if (getsockname(sock, &sa.u.sa, &sa_size) < 0)
    return 0;

  switch (sa.u.sa.sa_family) {
  case AF_INET6:
    return ntohs(sa.u.sin6.sin6_port);
  default:
    return ntohs(sa.u.sin.sin_port);
  }
}

TcpListener::TcpListener(int sock)
{
  fd = sock;
}

TcpListener::TcpListener(const TcpListener& other)
{
  fd = dupsocket (other.fd);
  // Hope TcpListener::shutdown(other) doesn't get called...
}

TcpListener& TcpListener::operator= (const TcpListener& other)
{
  if (this != &other)
  {
    closesocket (fd);
    fd = dupsocket (other.fd);
    // Hope TcpListener::shutdown(other) doesn't get called...
  }
  return *this;
}

TcpListener::TcpListener(const struct sockaddr *listenaddr,
                         socklen_t listenaddrlen)
{
  int one = 1;
  vnc_sockaddr_t sa;
  int sock;

  initSockets();

  if ((sock = socket (listenaddr->sa_family, SOCK_STREAM, 0)) < 0)
    throw SocketException("unable to create listening socket", errorNumber);

  memcpy (&sa, listenaddr, listenaddrlen);
#ifdef IPV6_V6ONLY
  if (listenaddr->sa_family == AF_INET6) {
    if (setsockopt (sock, IPPROTO_IPV6, IPV6_V6ONLY, (char*)&one, sizeof(one)))
      throw SocketException("unable to set IPV6_V6ONLY", errorNumber);
  }
#endif /* defined(IPV6_V6ONLY) */

#ifdef FD_CLOEXEC
  // - By default, close the socket on exec()
  fcntl(sock, F_SETFD, FD_CLOEXEC);
#endif

  // SO_REUSEADDR is broken on Windows. It allows binding to a port
  // that already has a listening socket on it. SO_EXCLUSIVEADDRUSE
  // might do what we want, but requires investigation.
#ifndef WIN32
  if (setsockopt(sock, SOL_SOCKET, SO_REUSEADDR,
                 (char *)&one, sizeof(one)) < 0) {
    int e = errorNumber;
    closesocket(sock);
>>>>>>> 4c33f2ca86586bb8461526b93cba57a0a14c8baa
    throw SocketException("unable to create listening socket", e);
  }
#endif

<<<<<<< HEAD
  // - Bind it to the desired port
  struct sockaddr_in addr;
  memset(&addr, 0, sizeof(addr));
  addr.sin_family = AF_INET;

  if (localhostOnly) {
    addr.sin_addr.s_addr = htonl(INADDR_LOOPBACK);
  } else if (listenaddr != NULL) {
#ifdef HAVE_INET_ATON
    if (inet_aton(listenaddr, &addr.sin_addr) == 0)
#else
    /* Some systems (e.g. Windows) do not have inet_aton, sigh */
    if ((addr.sin_addr.s_addr = inet_addr(listenaddr)) == INADDR_NONE)
#endif
    {
      closesocket(fd);
      throw Exception("invalid network interface address: %s", listenaddr);
    }
  } else
    addr.sin_addr.s_addr = htonl(INADDR_ANY); /* Bind to 0.0.0.0 by default. */

  addr.sin_port = htons(port);
  if (bind(fd, (struct sockaddr *)&addr, sizeof(addr)) < 0) {
    int e = errorNumber;
    closesocket(fd);
    throw SocketException("unable to bind listening socket", e);
  }

  // - Set it to be a listening socket
  if (listen(fd, 5) < 0) {
    int e = errorNumber;
    closesocket(fd);
    throw SocketException("unable to set socket to listening mode", e);
  }
}

TcpListener::~TcpListener() {
  if (closeFd) closesocket(fd);
=======
  if (bind(sock, &sa.u.sa, listenaddrlen) == -1) {
    closesocket(sock);
    throw SocketException("failed to bind socket", errorNumber);
  }

  // - Set it to be a listening socket
  if (listen(sock, 5) < 0) {
    int e = errorNumber;
    closesocket(sock);
    throw SocketException("unable to set socket to listening mode", e);
  }

  fd = sock;
}

TcpListener::~TcpListener() {
  closesocket(fd);
>>>>>>> 4c33f2ca86586bb8461526b93cba57a0a14c8baa
}

void TcpListener::shutdown()
{
#ifdef WIN32
  closesocket(getFd());
#else
  ::shutdown(getFd(), 2);
#endif
}


Socket*
TcpListener::accept() {
  int new_sock = -1;

  // Accept an incoming connection
  if ((new_sock = ::accept(fd, 0, 0)) < 0)
    throw SocketException("unable to accept new connection", errorNumber);

#ifndef WIN32
  // - By default, close the socket on exec()
  fcntl(new_sock, F_SETFD, FD_CLOEXEC);
#endif

  // Disable Nagle's algorithm, to reduce latency
  TcpSocket::enableNagles(new_sock, false);

  // Create the socket object & check connection is allowed
  TcpSocket* s = new TcpSocket(new_sock);
  if (filter && !filter->verifyConnection(s)) {
    delete s;
    return 0;
  }
  return s;
}

void TcpListener::getMyAddresses(std::list<char*>* result) {
<<<<<<< HEAD
  const hostent* addrs = gethostbyname(0);
  if (addrs == 0)
    throw rdr::SystemException("gethostbyname", errorNumber);
  if (addrs->h_addrtype != AF_INET)
    throw rdr::Exception("getMyAddresses: bad family");
  for (int i=0; addrs->h_addr_list[i] != 0; i++) {
    const char* addrC = inet_ntoa(*((struct in_addr*)addrs->h_addr_list[i]));
    char* addr = new char[strlen(addrC)+1];
    strcpy(addr, addrC);
    result->push_back(addr);
  }
=======
  struct addrinfo *ai, *current, hints;

  initSockets();

  memset(&hints, 0, sizeof(struct addrinfo));
  hints.ai_flags = AI_PASSIVE | AI_NUMERICSERV;
  hints.ai_family = AF_UNSPEC;
  hints.ai_socktype = SOCK_STREAM;
  hints.ai_canonname = NULL;
  hints.ai_addr = NULL;
  hints.ai_next = NULL;

  // Windows doesn't like NULL for service, so specify something
  if ((getaddrinfo(NULL, "1", &hints, &ai)) != 0)
    return;

  for (current= ai; current != NULL; current = current->ai_next) {
    switch (current->ai_family) {
    case AF_INET:
      if (!UseIPv4)
        continue;
      break;
    case AF_INET6:
      if (!UseIPv6)
        continue;
      break;
    default:
      continue;
    }

    char *addr = new char[INET6_ADDRSTRLEN];

    getnameinfo(current->ai_addr, current->ai_addrlen, addr, INET6_ADDRSTRLEN,
                NULL, 0, NI_NUMERICHOST);

    result->push_back(addr);
  }

  freeaddrinfo(ai);
>>>>>>> 4c33f2ca86586bb8461526b93cba57a0a14c8baa
}

int TcpListener::getMyPort() {
  return TcpSocket::getSockPort(getFd());
}


<<<<<<< HEAD
=======
void network::createLocalTcpListeners(std::list<TcpListener> *listeners,
                                      int port)
{
  std::list<TcpListener> new_listeners;
  vnc_sockaddr_t sa;

  initSockets();

  if (UseIPv6) {
    sa.u.sin6.sin6_family = AF_INET6;
    sa.u.sin6.sin6_port = htons (port);
    sa.u.sin6.sin6_addr = in6addr_loopback;
    try {
      new_listeners.push_back (TcpListener (&sa.u.sa, sizeof (sa.u.sin6)));
    } catch (SocketException& e) {
      // Ignore this if it is due to lack of address family support on
      // the interface or on the system
      if (e.err != EADDRNOTAVAIL && e.err != EAFNOSUPPORT)
        // Otherwise, report the error
        throw;
    }
  }
  if (UseIPv4) {
    sa.u.sin.sin_family = AF_INET;
    sa.u.sin.sin_port = htons (port);
    sa.u.sin.sin_addr.s_addr = htonl (INADDR_LOOPBACK);
    try {
      new_listeners.push_back (TcpListener (&sa.u.sa, sizeof (sa.u.sin)));
    } catch (SocketException& e) {
      // Ignore this if it is due to lack of address family support on
      // the interface or on the system
      if (e.err != EADDRNOTAVAIL && e.err != EAFNOSUPPORT)
        // Otherwise, report the error
        throw;
    }
  }

  if (new_listeners.empty ())
    throw SocketException("createLocalTcpListeners: no addresses available",
                          EADDRNOTAVAIL);

  listeners->splice (listeners->end(), new_listeners);
}

void network::createTcpListeners(std::list<TcpListener> *listeners,
                                 const char *addr,
                                 int port)
{
  std::list<TcpListener> new_listeners;

  struct addrinfo *ai, *current, hints;
  char service[16];
  int result;

  initSockets();

  memset(&hints, 0, sizeof(struct addrinfo));
  hints.ai_flags = AI_PASSIVE | AI_NUMERICSERV;
  hints.ai_family = AF_UNSPEC;
  hints.ai_socktype = SOCK_STREAM;
  hints.ai_canonname = NULL;
  hints.ai_addr = NULL;
  hints.ai_next = NULL;

  snprintf (service, sizeof (service) - 1, "%d", port);
  service[sizeof (service) - 1] = '\0';
  if ((result = getaddrinfo(addr, service, &hints, &ai)) != 0)
    throw rdr::Exception("unable to resolve listening address: %s",
                         gai_strerror(result));

  for (current = ai; current != NULL; current = current->ai_next) {
    switch (current->ai_family) {
    case AF_INET:
      if (!UseIPv4)
        continue;
      break;

    case AF_INET6:
      if (!UseIPv6)
        continue;
      break;

    default:
      continue;
    }

    try {
      new_listeners.push_back(TcpListener (current->ai_addr,
                                           current->ai_addrlen));
    } catch (SocketException& e) {
      // Ignore this if it is due to lack of address family support on
      // the interface or on the system
      if (e.err != EADDRNOTAVAIL && e.err != EAFNOSUPPORT) {
        // Otherwise, report the error
        freeaddrinfo(ai);
        throw;
      }
    }
  }
  freeaddrinfo(ai);

  if (new_listeners.empty ())
    throw SocketException("createTcpListeners: no addresses available",
                          EADDRNOTAVAIL);

  listeners->splice (listeners->end(), new_listeners);
}


>>>>>>> 4c33f2ca86586bb8461526b93cba57a0a14c8baa
TcpFilter::TcpFilter(const char* spec) {
  rfb::CharArray tmp;
  tmp.buf = rfb::strDup(spec);
  while (tmp.buf) {
    rfb::CharArray first;
    rfb::strSplit(tmp.buf, ',', &first.buf, &tmp.buf);
    if (strlen(first.buf))
      filter.push_back(parsePattern(first.buf));
  }
}

TcpFilter::~TcpFilter() {
}


static bool
<<<<<<< HEAD
patternMatchIP(const TcpFilter::Pattern& pattern, const char* value) {
  unsigned long address = inet_addr((char *)value);
  if (address == INADDR_NONE) return false;
  return ((pattern.address & pattern.mask) == (address & pattern.mask));
=======
patternMatchIP(const TcpFilter::Pattern& pattern, vnc_sockaddr_t *sa) {
  switch (pattern.address.u.sa.sa_family) {
    unsigned long address;

  case AF_INET:
    if (sa->u.sa.sa_family != AF_INET)
      return false;

    address = sa->u.sin.sin_addr.s_addr;
    if (address == htonl (INADDR_NONE)) return false;
    return ((pattern.address.u.sin.sin_addr.s_addr &
             pattern.mask.u.sin.sin_addr.s_addr) ==
            (address & pattern.mask.u.sin.sin_addr.s_addr));

  case AF_INET6:
    if (sa->u.sa.sa_family != AF_INET6)
      return false;

    for (unsigned int n = 0; n < 16; n++) {
      unsigned int bits = (n + 1) * 8;
      unsigned int mask;
      if (pattern.prefixlen > bits)
        mask = 0xff;
      else {
        unsigned int lastbits = 0xff;
        lastbits <<= bits - pattern.prefixlen;
        mask = lastbits & 0xff;
      }

      if ((pattern.address.u.sin6.sin6_addr.s6_addr[n] & mask) !=
          (sa->u.sin6.sin6_addr.s6_addr[n] & mask))
        return false;

      if (mask < 0xff)
        break;
    }

    return true;

  case AF_UNSPEC:
    // Any address matches
    return true;

  default:
    break;
  }

  return false;
>>>>>>> 4c33f2ca86586bb8461526b93cba57a0a14c8baa
}

bool
TcpFilter::verifyConnection(Socket* s) {
  rfb::CharArray name;
<<<<<<< HEAD
=======
  vnc_sockaddr_t sa;
  socklen_t sa_size = sizeof(sa);

  if (getpeername(s->getFd(), &sa.u.sa, &sa_size) != 0)
    return false;
>>>>>>> 4c33f2ca86586bb8461526b93cba57a0a14c8baa

  name.buf = s->getPeerAddress();
  std::list<TcpFilter::Pattern>::iterator i;
  for (i=filter.begin(); i!=filter.end(); i++) {
<<<<<<< HEAD
    if (patternMatchIP(*i, name.buf)) {
=======
    if (patternMatchIP(*i, &sa)) {
>>>>>>> 4c33f2ca86586bb8461526b93cba57a0a14c8baa
      switch ((*i).action) {
      case Accept:
        vlog.debug("ACCEPT %s", name.buf);
        return true;
      case Query:
        vlog.debug("QUERY %s", name.buf);
        s->setRequiresQuery();
        return true;
      case Reject:
        vlog.debug("REJECT %s", name.buf);
        return false;
      }
    }
  }

  vlog.debug("[REJECT] %s", name.buf);
  return false;
}


TcpFilter::Pattern TcpFilter::parsePattern(const char* p) {
  TcpFilter::Pattern pattern;

<<<<<<< HEAD
  bool expandMask = false;
  rfb::CharArray addr, mask;

  if (rfb::strSplit(&p[1], '/', &addr.buf, &mask.buf)) {
    if (rfb::strContains(mask.buf, '.')) {
      pattern.mask = inet_addr(mask.buf);
    } else {
      pattern.mask = atoi(mask.buf);
      expandMask = true;
    }
  } else {
    pattern.mask = 32;
    expandMask = true;
  }
  if (expandMask) {
    unsigned long expanded = 0;
    // *** check endianness!
    for (int i=0; i<(int)pattern.mask; i++)
      expanded |= 1<<(31-i);
    pattern.mask = htonl(expanded);
  }

  pattern.address = inet_addr(addr.buf) & pattern.mask;
  if ((pattern.address == INADDR_NONE) ||
      (pattern.address == 0)) pattern.mask = 0;
=======
  rfb::CharArray addr, pref;
  bool prefix_specified;
  int family;

  prefix_specified = rfb::strSplit(&p[1], '/', &addr.buf, &pref.buf);
  if (addr.buf[0] == '\0') {
    // Match any address
    memset (&pattern.address, 0, sizeof (pattern.address));
    pattern.address.u.sa.sa_family = AF_UNSPEC;
    pattern.prefixlen = 0;
  } else {
    struct addrinfo hints;
    struct addrinfo *ai;
    char *p = addr.buf;
    int result;
    memset (&hints, 0, sizeof (hints));
    hints.ai_family = AF_UNSPEC;
    hints.ai_flags = AI_NUMERICHOST;

    // Take out brackets, if present
    if (*p == '[') {
      size_t len;
      p++;
      len = strlen (p);
      if (len > 0 && p[len - 1] == ']')
        p[len - 1] = '\0';
    }

    if ((result = getaddrinfo (p, NULL, &hints, &ai)) != 0) {
      throw Exception("unable to resolve host by name: %s",
                      gai_strerror(result));
    }

    memcpy (&pattern.address.u.sa, ai->ai_addr, ai->ai_addrlen);
    freeaddrinfo (ai);

    family = pattern.address.u.sa.sa_family;

    if (prefix_specified) {
      if (family == AF_INET &&
          rfb::strContains(pref.buf, '.')) {
        throw Exception("mask no longer supported for filter, "
                        "use prefix instead");
      }

      pattern.prefixlen = (unsigned int) atoi(pref.buf);
    } else {
      switch (family) {
      case AF_INET:
        pattern.prefixlen = 32;
        break;
      case AF_INET6:
        pattern.prefixlen = 128;
        break;
      default:
        throw Exception("unknown address family");
      }
    }
  }

  family = pattern.address.u.sa.sa_family;

  if (pattern.prefixlen > (family == AF_INET ? 32: 128))
    throw Exception("invalid prefix length for filter address: %u",
                    pattern.prefixlen);

  // Compute mask from address and prefix length
  memset (&pattern.mask, 0, sizeof (pattern.mask));
  switch (family) {
    unsigned long mask;
  case AF_INET:
    mask = 0;
    for (unsigned int i=0; i<pattern.prefixlen; i++)
      mask |= 1<<(31-i);
    pattern.mask.u.sin.sin_addr.s_addr = htonl(mask);
    break;

  case AF_INET6:
    for (unsigned int n = 0; n < 16; n++) {
      unsigned int bits = (n + 1) * 8;
      if (pattern.prefixlen > bits)
        pattern.mask.u.sin6.sin6_addr.s6_addr[n] = 0xff;
      else {
        unsigned int lastbits = 0xff;
        lastbits <<= bits - pattern.prefixlen;
        pattern.mask.u.sin6.sin6_addr.s6_addr[n] = lastbits & 0xff;
        break;
      }
    }
    break;
  case AF_UNSPEC:
    // No mask to compute
    break;
  default:
    ; /* not reached */
  }
>>>>>>> 4c33f2ca86586bb8461526b93cba57a0a14c8baa

  switch(p[0]) {
  case '+': pattern.action = TcpFilter::Accept; break;
  case '-': pattern.action = TcpFilter::Reject; break;
  case '?': pattern.action = TcpFilter::Query; break;
  };

  return pattern;
}

char* TcpFilter::patternToStr(const TcpFilter::Pattern& p) {
<<<<<<< HEAD
  in_addr tmp;
  rfb::CharArray addr, mask;
  tmp.s_addr = p.address;
  addr.buf = rfb::strDup(inet_ntoa(tmp));
  tmp.s_addr = p.mask;
  mask.buf = rfb::strDup(inet_ntoa(tmp));
  char* result = new char[strlen(addr.buf)+1+strlen(mask.buf)+1+1];
  switch (p.action) {
  case Accept: result[0] = '+'; break;
  case Reject: result[0] = '-'; break;
  case Query: result[0] = '?'; break;
  };
  result[1] = 0;
  strcat(result, addr.buf);
  strcat(result, "/");
  strcat(result, mask.buf);
=======
  rfb::CharArray addr;
  char buffer[INET6_ADDRSTRLEN + 2];

  if (p.address.u.sa.sa_family == AF_INET) {
    getnameinfo(&p.address.u.sa, sizeof(p.address.u.sin),
                buffer, sizeof (buffer), NULL, 0, NI_NUMERICHOST);
    addr.buf = rfb::strDup(buffer);
  } else if (p.address.u.sa.sa_family == AF_INET6) {
    buffer[0] = '[';
    getnameinfo(&p.address.u.sa, sizeof(p.address.u.sin6),
                buffer + 1, sizeof (buffer) - 2, NULL, 0, NI_NUMERICHOST);
    strcat(buffer, "]");
    addr.buf = rfb::strDup(buffer);
  } else if (p.address.u.sa.sa_family == AF_UNSPEC)
    addr.buf = rfb::strDup("");

  char action;
  switch (p.action) {
  case Accept: action = '+'; break;
  case Reject: action = '-'; break;
  default:
  case Query: action = '?'; break;
  };
  size_t resultlen = (1                   // action
                      + strlen (addr.buf) // address
                      + 1                 // slash
                      + 3                 // prefix length, max 128
                      + 1);               // terminating nul
  char* result = new char[resultlen];
  if (addr.buf[0] == '\0')
    snprintf(result, resultlen, "%c", action);
  else
    snprintf(result, resultlen, "%c%s/%u", action, addr.buf, p.prefixlen);

>>>>>>> 4c33f2ca86586bb8461526b93cba57a0a14c8baa
  return result;
}
