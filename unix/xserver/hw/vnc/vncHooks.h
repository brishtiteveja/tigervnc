/* Copyright (C) 2002-2005 RealVNC Ltd.  All Rights Reserved.
<<<<<<< HEAD
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
#ifndef __VNCHOOKS_H__
#define __VNCHOOKS_H__

<<<<<<< HEAD
#ifdef HAVE_DIX_CONFIG_H
#include <dix-config.h>
#endif

extern "C" {
#include <screenint.h>
  extern Bool vncHooksInit(ScreenPtr pScreen, XserverDesktop* desktop);
}
=======
#ifdef __cplusplus
extern "C" {
#endif

int vncHooksInit(int scrIdx);

void vncGetScreenImage(int scrIdx, int x, int y, int width, int height,
                       char *buffer, int strideBytes);

#ifdef __cplusplus
}
#endif
>>>>>>> 4c33f2ca86586bb8461526b93cba57a0a14c8baa

#endif
