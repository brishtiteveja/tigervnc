/* Copyright (C) 2002-2005 RealVNC Ltd.  All Rights Reserved.
<<<<<<< HEAD
 * Copyright 2009-2011 Pierre Ossman for Cendio AB
=======
 * Copyright 2009-2015 Pierre Ossman for Cendio AB
>>>>>>> 4c33f2ca86586bb8461526b93cba57a0a14c8baa
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
//
// XserverDesktop.h
//

#ifndef __XSERVERDESKTOP_H__
#define __XSERVERDESKTOP_H__

#ifdef HAVE_DIX_CONFIG_H
#include <dix-config.h>
#endif

#include <map>

<<<<<<< HEAD
=======
#include <stdint.h>

>>>>>>> 4c33f2ca86586bb8461526b93cba57a0a14c8baa
#include <rfb/SDesktop.h>
#include <rfb/HTTPServer.h>
#include <rfb/PixelBuffer.h>
#include <rfb/Configuration.h>
#include <rfb/VNCServerST.h>
#include <rdr/SubstitutingInStream.h>
#include "Input.h"

<<<<<<< HEAD
extern "C" {
#define class c_class
#include <scrnintstr.h>
#include <os.h>
#ifdef RANDR
#include <randrstr.h>
#endif
#undef class
}

=======
>>>>>>> 4c33f2ca86586bb8461526b93cba57a0a14c8baa
namespace rfb {
  class VNCServerST;
}

namespace network { class TcpListener; class Socket; }

class XserverDesktop : public rfb::SDesktop, public rfb::FullFramePixelBuffer,
                       public rdr::Substitutor,
                       public rfb::VNCServerST::QueryConnectionHandler {
public:

<<<<<<< HEAD
  XserverDesktop(ScreenPtr pScreen, network::TcpListener* listener,
                 network::TcpListener* httpListener_,
                 const char* name, const rfb::PixelFormat &pf,
                 void* fbptr, int stride);
=======
  XserverDesktop(int screenIndex,
                 std::list<network::TcpListener> listeners_,
                 std::list<network::TcpListener> httpListeners_,
                 const char* name, const rfb::PixelFormat &pf,
                 int width, int height, void* fbptr, int stride);
>>>>>>> 4c33f2ca86586bb8461526b93cba57a0a14c8baa
  virtual ~XserverDesktop();

  // methods called from X server code
  void blockUpdates();
  void unblockUpdates();
  void setFramebuffer(int w, int h, void* fbptr, int stride);
  void refreshScreenLayout();
  void bell();
  void serverCutText(const char* str, int len);
  void setDesktopName(const char* name);
<<<<<<< HEAD
  void setCursor(CursorPtr cursor);
  void add_changed(RegionPtr reg);
  void add_copied(RegionPtr dst, int dx, int dy);
  void ignoreHooks(bool b) { ignoreHooks_ = b; }
  void blockHandler(fd_set* fds, OSTimePtr timeout);
  void wakeupHandler(fd_set* fds, int nfds);
  void writeBlockHandler(fd_set* fds);
=======
  void setCursor(int width, int height, int hotX, int hotY,
                 const unsigned char *rgbaData);
  void add_changed(const rfb::Region &region);
  void add_copied(const rfb::Region &dest, const rfb::Point &delta);
  void readBlockHandler(fd_set* fds, struct timeval ** timeout);
  void readWakeupHandler(fd_set* fds, int nfds);
  void writeBlockHandler(fd_set* fds, struct timeval ** timeout);
>>>>>>> 4c33f2ca86586bb8461526b93cba57a0a14c8baa
  void writeWakeupHandler(fd_set* fds, int nfds);
  void addClient(network::Socket* sock, bool reverse);
  void disconnectClients();

  // QueryConnect methods called from X server code
<<<<<<< HEAD
  // getQueryTimeout()
  //   Returns the timeout associated with a particular
  //   connection, identified by an opaque Id passed to the
  //   X code earlier.  Also optionally gets the address and
  //   name associated with that connection.
  //   Returns zero if the Id is not recognised.
  int getQueryTimeout(void* opaqueId,
                      const char** address=0,
                      const char** username=0);

  // approveConnection()
  //   Used by X server code to supply the result of a query.
  void approveConnection(void* opaqueId, bool accept,
=======
  // getQueryConnect()
  //   Returns information about the currently waiting query
  //   (or an id of 0 if there is none waiting)
  void getQueryConnect(uint32_t* opaqueId, const char** address,
                       const char** username, int *timeout);

  // approveConnection()
  //   Used by X server code to supply the result of a query.
  void approveConnection(uint32_t opaqueId, bool accept,
>>>>>>> 4c33f2ca86586bb8461526b93cba57a0a14c8baa
                         const char* rejectMsg=0);

  // rfb::SDesktop callbacks
  virtual void pointerEvent(const rfb::Point& pos, int buttonMask);
  virtual void keyEvent(rdr::U32 key, bool down);
  virtual void clientCutText(const char* str, int len);
  virtual rfb::Point getFbSize() { return rfb::Point(width(), height()); }
  virtual unsigned int setScreenLayout(int fb_width, int fb_height,
                                       const rfb::ScreenSet& layout);

  // rfb::PixelBuffer callbacks
  virtual void grabRegion(const rfb::Region& r);

  // rdr::Substitutor callback
  virtual char* substitute(const char* varName);

  // rfb::VNCServerST::QueryConnectionHandler callback
  virtual rfb::VNCServerST::queryResult queryConnection(network::Socket* sock,
                                                        const char* userName,
                                                        char** reason);

private:
  rfb::ScreenSet computeScreenLayout();
<<<<<<< HEAD
#ifdef RANDR
  RRModePtr findRandRMode(RROutputPtr output, int width, int height);
#endif

  ScreenPtr pScreen;
  rfb::VNCServerST* server;
  rfb::HTTPServer* httpServer;
  network::TcpListener* listener;
  network::TcpListener* httpListener;
  bool deferredUpdateTimerSet;
  bool grabbing;
  bool ignoreHooks_;
  bool directFbptr;

  void* queryConnectId;
=======

  int screenIndex;
  rfb::VNCServerST* server;
  rfb::HTTPServer* httpServer;
  std::list<network::TcpListener> listeners;
  std::list<network::TcpListener> httpListeners;
  bool deferredUpdateTimerSet;
  bool directFbptr;
  struct timeval dixTimeout;

  uint32_t queryConnectId;
  network::Socket* queryConnectSocket;
>>>>>>> 4c33f2ca86586bb8461526b93cba57a0a14c8baa
  rfb::CharArray queryConnectAddress;
  rfb::CharArray queryConnectUsername;

#ifdef RANDR
<<<<<<< HEAD
  typedef std::map<RROutputPtr, rdr::U32> OutputIdMap;
=======
  typedef std::map<intptr_t, rdr::U32> OutputIdMap;
>>>>>>> 4c33f2ca86586bb8461526b93cba57a0a14c8baa
  OutputIdMap outputIdMap;
#endif

  rfb::Point oldCursorPos;
};
#endif
