%define _default_patch_fuzz 2
<<<<<<< HEAD
%define mesa_version 7.7.1
=======
%define tigervnc_src_dir %{_builddir}/%{name}-%{version}%{?snap:-%{snap}}
%define xorg_buildroot %{tigervnc_src_dir}/xorg.build
>>>>>>> 4c33f2ca86586bb8461526b93cba57a0a14c8baa
%{!?_self_signed: %define _self_signed 1}

Name: tigervnc
Version: @VERSION@
<<<<<<< HEAD
Release: 18%{?snap:.%{snap}}%{?dist}
=======
Release: 6%{?snap:.%{snap}}%{?dist}
>>>>>>> 4c33f2ca86586bb8461526b93cba57a0a14c8baa
Summary: A TigerVNC remote display system

Group: User Interface/Desktops
License: GPLv2+
Packager: Brian P. Hinz <bphinz@users.sourceforge.net>
URL: http://www.tigervnc.com

Source0: %{name}-%{version}%{?snap:-%{snap}}.tar.bz2
Source1: vncserver.service
Source2: vncserver.sysconfig
Source6: vncviewer.desktop
Source9: FindX11.cmake
<<<<<<< HEAD
Source11: http://fltk.org/pub/fltk/1.3.2/fltk-1.3.2-source.tar.gz
Source12: http://downloads.sourceforge.net/project/libjpeg-turbo/1.3.0/libjpeg-turbo-1.3.0.tar.gz

# http://ftp.redhat.com/pub/redhat/linux/enterprise/6Client/en/os/SRPMS/xorg-x11-proto-devel-7.6-13.el6.src.rpm
# http://ftp.redhat.com/pub/redhat/linux/enterprise/6Client/en/os/SRPMS/
Source98: http://www.x.org/releases/X11R7.5/src/util/makedepend-1.0.2.tar.bz2
Source99: http://xcb.freedesktop.org/dist/libpthread-stubs-0.3.tar.bz2
Source100: http://www.x.org/releases/X11R7.5/src/lib/libICE-1.0.6.tar.bz2
Source101: http://www.x.org/releases/X11R7.5/src/lib/libSM-1.1.1.tar.bz2
Source102: http://www.x.org/releases/X11R7.5/src/lib/libX11-1.3.2.tar.bz2
Source103: http://www.x.org/releases/X11R7.5/src/lib/libXScrnSaver-1.2.0.tar.bz2
Source104: http://www.x.org/releases/X11R7.5/src/lib/libXau-1.0.5.tar.bz2
Source105: http://www.x.org/releases/X11R7.5/src/lib/libXaw-1.0.7.tar.bz2
Source106: http://www.x.org/releases/X11R7.5/src/lib/libXcomposite-0.4.1.tar.bz2
Source107: http://www.x.org/releases/X11R7.5/src/lib/libXcursor-1.1.10.tar.bz2
Source108: http://www.x.org/releases/X11R7.5/src/lib/libXdamage-1.1.2.tar.bz2
Source109: http://www.x.org/releases/X11R7.5/src/lib/libXdmcp-1.0.3.tar.bz2
Source110: http://www.x.org/releases/individual/lib/libXext-1.1.tar.bz2
Source111: http://www.x.org/releases/X11R7.5/src/lib/libXfixes-4.0.4.tar.bz2
Source112: http://www.x.org/releases/X11R7.5/src/lib/libXfont-1.4.1.tar.bz2
Source113: http://www.x.org/releases/X11R7.5/src/lib/libXft-2.1.14.tar.bz2
Source114: http://www.x.org/releases/X11R7.5/src/lib/libXi-1.3.tar.bz2
Source115: http://www.x.org/releases/X11R7.5/src/lib/libXinerama-1.1.tar.bz2
Source116: http://www.x.org/releases/X11R7.5/src/lib/libXmu-1.0.5.tar.bz2
Source117: http://www.x.org/releases/X11R7.5/src/lib/libXpm-3.5.8.tar.bz2
Source118: http://www.x.org/releases/X11R7.5/src/lib/libXrandr-1.3.0.tar.bz2
Source119: http://www.x.org/releases/X11R7.5/src/lib/libXrender-0.9.5.tar.bz2
Source120: http://www.x.org/releases/X11R7.5/src/lib/libXt-1.0.7.tar.bz2
Source121: http://www.x.org/releases/X11R7.5/src/lib/libXtst-1.1.0.tar.bz2
Source122: http://www.x.org/releases/X11R7.5/src/lib/libXv-1.0.5.tar.bz2
Source123: http://www.x.org/releases/X11R7.5/src/lib/libXvMC-1.0.5.tar.bz2
Source124: http://www.x.org/releases/X11R7.5/src/lib/libXxf86dga-1.1.1.tar.bz2
Source125: http://www.x.org/releases/X11R7.5/src/lib/libXxf86vm-1.1.0.tar.bz2
Source126: http://www.x.org/releases/X11R7.5/src/lib/libfontenc-1.0.5.tar.bz2
Source127: http://www.x.org/releases/X11R7.5/src/lib/libpciaccess-0.10.9.tar.bz2
Source128: http://www.x.org/releases/X11R7.5/src/lib/libxkbfile-1.0.6.tar.bz2
Source129: http://www.x.org/releases/X11R7.5/src/lib/xtrans-1.2.5.tar.bz2
Source130: http://xorg.freedesktop.org/archive/individual/proto/bigreqsproto-1.1.0.tar.bz2
Source131: http://xorg.freedesktop.org/archive/individual/proto/compositeproto-0.4.1.tar.bz2
Source132: http://xorg.freedesktop.org/archive/individual/proto/damageproto-1.2.0.tar.bz2
Source133: http://xorg.freedesktop.org/archive/individual/proto/evieext-1.1.1.tar.bz2
Source134: http://xorg.freedesktop.org/archive/individual/proto/fixesproto-5.0.tar.bz2
Source135: http://xorg.freedesktop.org/archive/individual/proto/fontsproto-2.1.0.tar.bz2
Source136: http://xorg.freedesktop.org/archive/individual/proto/glproto-1.4.12.tar.bz2
Source137: http://xorg.freedesktop.org/archive/individual/proto/inputproto-2.0.2.tar.bz2
Source138: http://xorg.freedesktop.org/archive/individual/proto/kbproto-1.0.5.tar.bz2
Source139: http://xorg.freedesktop.org/archive/individual/proto/randrproto-1.3.1.tar.bz2
#Source139: http://xorg.freedesktop.org/archive/individual/proto/randrproto-20110224-git105a161.tar.bz2
Source140: http://xorg.freedesktop.org/archive/individual/proto/recordproto-1.14.1.tar.bz2
Source141: http://xorg.freedesktop.org/archive/individual/proto/renderproto-0.11.1.tar.bz2
Source142: http://xorg.freedesktop.org/archive/individual/proto/resourceproto-1.2.0.tar.bz2
Source143: http://xorg.freedesktop.org/archive/individual/proto/scrnsaverproto-1.2.1.tar.bz2
Source144: http://xorg.freedesktop.org/archive/individual/proto/videoproto-2.3.1.tar.bz2
Source145: http://xorg.freedesktop.org/archive/individual/proto/xcmiscproto-1.2.1.tar.bz2
Source146: http://xorg.freedesktop.org/archive/individual/proto/xextproto-7.2.0.tar.bz2
Source147: http://xorg.freedesktop.org/archive/individual/proto/xf86bigfontproto-1.2.0.tar.bz2
Source148: http://xorg.freedesktop.org/archive/individual/proto/xf86dgaproto-2.1.tar.bz2
Source149: http://xorg.freedesktop.org/archive/individual/proto/xf86driproto-2.1.1.tar.bz2
Source150: http://xorg.freedesktop.org/archive/individual/proto/xf86miscproto-0.9.3.tar.bz2
Source151: http://xorg.freedesktop.org/archive/individual/proto/xf86vidmodeproto-2.3.1.tar.bz2
Source152: http://xorg.freedesktop.org/archive/individual/proto/xineramaproto-1.2.1.tar.bz2
Source153: http://xorg.freedesktop.org/archive/individual/proto/xproto-7.0.22.tar.bz2
Source154: http://xorg.freedesktop.org/archive/individual/proto/dri2proto-2.3.tar.bz2

#Source130: http://www.x.org/releases/X11R7.5/src/proto/bigreqsproto-1.1.0.tar.bz2
#Source131: http://www.x.org/releases/X11R7.5/src/proto/compositeproto-0.4.1.tar.bz2
#Source132: http://www.x.org/releases/X11R7.5/src/proto/damageproto-1.2.0.tar.bz2
#Source133: http://www.x.org/releases/X11R7.5/src/proto/dri2proto-2.3.tar.bz2
#Source134: http://www.x.org/releases/X11R7.5/src/proto/fixesproto-5.0.tar.bz2
#Source135: http://www.x.org/releases/X11R7.5/src/proto/fontsproto-2.1.0.tar.bz2
#Source136: http://www.x.org/releases/X11R7.5/src/proto/glproto-1.4.12.tar.bz2
#Source137: http://www.x.org/releases/X11R7.5/src/proto/inputproto-2.0.2.tar.bz2
#Source138: http://www.x.org/releases/X11R7.5/src/proto/kbproto-1.0.5.tar.bz2
#Source139: http://www.x.org/releases/X11R7.5/src/proto/randrproto-20110224-git105a161.tar.bz2
#Source140: http://www.x.org/releases/X11R7.5/src/proto/recordproto-1.14.1.tar.bz2
#Source141: http://www.x.org/releases/X11R7.5/src/proto/renderproto-0.11.1.tar.bz2
#Source142: http://www.x.org/releases/X11R7.5/src/proto/resourceproto-1.2.0.tar.bz2
#Source143: http://www.x.org/releases/X11R7.5/src/proto/scrnsaverproto-1.2.1.tar.bz2
#Source144: http://www.x.org/releases/X11R7.5/src/proto/videoproto-2.3.1.tar.bz2
#Source145: http://www.x.org/releases/X11R7.5/src/proto/xcmiscproto-1.2.1.tar.bz2
#Source146: http://www.x.org/releases/X11R7.5/src/proto/xextproto-7.2.0.tar.bz2
#Source147: http://www.x.org/releases/X11R7.5/src/proto/xf86bigfontproto-1.2.0.tar.bz2
#Source148: http://www.x.org/releases/X11R7.5/src/proto/xf86dgaproto-2.1.tar.bz2
#Source149: http://www.x.org/releases/X11R7.5/src/proto/xf86driproto-2.1.1.tar.bz2
#Source150: http://www.x.org/releases/X11R7.5/src/proto/xf86vidmodeproto-2.3.1.tar.bz2
#Source151: http://www.x.org/releases/X11R7.5/src/proto/xproto-7.0.22.tar.bz2

Source155: http://www.x.org/releases/individual/util/util-macros-1.4.1.tar.bz2
Source156: http://www.x.org/pub/individual/xserver/xorg-server-1.7.7.tar.bz2
#Source157: ftp://ftp.x.org/pub/individual/app/xauth-1.0.2.tar.bz2
#Source158: http://www.x.org/releases/X11R7.5/src/everything/xkbutils-1.0.2.tar.bz2
Source159: http://dri.freedesktop.org/libdrm/libdrm-2.4.15.tar.bz2
Source160: http://downloads.sourceforge.net/project/freetype/freetype2/2.3.11/freetype-2.3.11.tar.bz2
Source161: ftp://ftp.freedesktop.org/pub/mesa/older-versions/7.x/%{mesa_version}/MesaLib-%{mesa_version}.tar.bz2
Source162: http://cgit.freedesktop.org/pixman/snapshot/pixman-0.26.0.tar.gz
Source163: http://www.x.org/releases/X11R7.5/src/lib/libXres-1.0.4.tar.bz2
Source164: http://www.x.org/releases/individual/lib/libXxf86misc-1.0.2.tar.bz2

Source200: http://fontconfig.org/release/fontconfig-2.4.1.tar.gz
Source201: 25-no-hint-fedora.conf
Source202: 30-aliases-fedora.conf
Source203: 40-generic-fedora.conf
Source204: 64-nonlatin-fedora.conf
Source205: 75-blacklist-fedora.conf

Source210: fc-cache.1
Source211: fc-cat.1
Source212: fc-list.1
Source213: fc-match.1

# FIXME:
# need to apply any patches in from the F12 srpms
# http://dl.fedoraproject.org/pub/archive/fedora/linux/releases/12/Fedora/source/SRPMS/mesa-7.6-0.13.fc12.src.rpm
# http://dl.fedoraproject.org/pub/archive/fedora/linux/releases/12/Fedora/source/SRPMS/pixman-0.16.2-1.fc12.src.rpm
# http://vault.centos.org/6.3/os/Source/SPackages/pixman-0.18.4-1.el6_0.1.src.rpm
# http://archive.fedoraproject.org/pub/archive/fedora/linux/releases/12/Everything/source/SRPMS/libdrm-2.4.15-4.fc12.src.rpm
# http://dl.fedoraproject.org/pub/archive/fedora/linux/releases/12/Fedora/source/SRPMS/freetype-2.3.9-6.fc12.src.rpm

BuildRoot: %{_tmppath}/%{name}-%{version}%{?snap:-%{snap}}-%{release}-root-%(%{__id_u} -n)

BuildRequires: automake >= 1.7, autoconf >= 2.57, libtool >= 1.4, gettext >= 0.14.4, gettext-devel >= 0.14.4, bison-devel
BuildRequires: openssl-devel
BuildRequires: desktop-file-utils, java-devel, jpackage-utils
BuildRequires: gnutls-devel, pam-devel
=======
Source11: http://fltk.org/pub/fltk/1.3.3/fltk-1.3.3-source.tar.gz
Source12: http://downloads.sourceforge.net/project/libjpeg-turbo/1.3.0/libjpeg-turbo-1.3.0.tar.gz
Source13: http://downloads.sourceforge.net/project/libpng/libpng15/older-releases/1.5.10/libpng-1.5.10.tar.bz2
Source14: https://ftp.gnu.org/gnu/gmp/gmp-6.0.0a.tar.bz2
Source15: http://ftp.gnu.org/gnu/libtasn1/libtasn1-4.2.tar.gz
Source16: https://ftp.gnu.org/gnu/nettle/nettle-2.7.1.tar.gz
Source17: ftp://ftp.gnutls.org/gcrypt/gnutls/v3.3/gnutls-3.3.13.tar.xz

Source100: http://www.x.org/releases/X11R7.7/src/everything/bigreqsproto-1.1.2.tar.bz2
Source101: http://www.x.org/releases/X11R7.7/src/everything/compositeproto-0.4.2.tar.bz2
Source102: http://www.x.org/releases/X11R7.7/src/everything/damageproto-1.2.1.tar.bz2
Source103: http://www.x.org/releases/X11R7.7/src/everything/dmxproto-2.3.1.tar.bz2
Source104: http://www.x.org/releases/X11R7.7/src/everything/dri2proto-2.6.tar.bz2
Source105: http://www.x.org/releases/X11R7.7/src/everything/fixesproto-5.0.tar.bz2
Source106: http://www.x.org/releases/X11R7.7/src/everything/font-util-1.3.0.tar.bz2
Source107: http://www.x.org/releases/X11R7.7/src/everything/fontsproto-2.1.2.tar.bz2
Source108: http://www.x.org/releases/X11R7.7/src/everything/glproto-1.4.15.tar.bz2
Source109: http://www.x.org/releases/X11R7.7/src/everything/inputproto-2.2.tar.bz2
Source110: http://www.x.org/releases/X11R7.7/src/everything/kbproto-1.0.6.tar.bz2
Source111: http://www.x.org/releases/X11R7.7/src/everything/libICE-1.0.8.tar.bz2
Source112: http://www.x.org/releases/X11R7.7/src/everything/libSM-1.2.1.tar.bz2
Source113: http://www.x.org/releases/X11R7.7/src/everything/libX11-1.5.0.tar.bz2
Source114: http://www.x.org/releases/X11R7.7/src/everything/libXScrnSaver-1.2.2.tar.bz2
Source115: http://www.x.org/releases/X11R7.7/src/everything/libXau-1.0.7.tar.bz2
Source116: http://www.x.org/releases/X11R7.7/src/everything/libXaw-1.0.11.tar.bz2
Source117: http://www.x.org/releases/X11R7.7/src/everything/libXcomposite-0.4.3.tar.bz2
Source118: http://www.x.org/releases/X11R7.7/src/everything/libXcursor-1.1.13.tar.bz2
Source119: http://www.x.org/releases/X11R7.7/src/everything/libXdamage-1.1.3.tar.bz2
Source120: http://www.x.org/releases/X11R7.7/src/everything/libXdmcp-1.1.1.tar.bz2
Source121: http://www.x.org/releases/X11R7.7/src/everything/libXext-1.3.1.tar.bz2
Source122: http://www.x.org/releases/X11R7.7/src/everything/libXfixes-5.0.tar.bz2
Source123: http://www.x.org/releases/X11R7.7/src/everything/libXfont-1.4.5.tar.bz2
Source124: http://www.x.org/releases/X11R7.7/src/everything/libXft-2.3.1.tar.bz2
Source125: http://www.x.org/releases/X11R7.7/src/everything/libXi-1.6.1.tar.bz2
Source126: http://www.x.org/releases/X11R7.7/src/everything/libXinerama-1.1.2.tar.bz2
Source127: http://www.x.org/releases/X11R7.7/src/everything/libXmu-1.1.1.tar.bz2
Source128: http://www.x.org/releases/X11R7.7/src/everything/libXpm-3.5.10.tar.bz2
Source129: http://www.x.org/releases/X11R7.7/src/everything/libXrandr-1.3.2.tar.bz2
Source130: http://www.x.org/releases/X11R7.7/src/everything/libXrender-0.9.7.tar.bz2
Source131: http://www.x.org/releases/X11R7.7/src/everything/libXres-1.0.6.tar.bz2
Source132: http://www.x.org/releases/X11R7.7/src/everything/libXt-1.1.3.tar.bz2
Source133: http://www.x.org/releases/X11R7.7/src/everything/libXtst-1.2.1.tar.bz2
Source134: http://www.x.org/releases/X11R7.7/src/everything/libXv-1.0.7.tar.bz2
Source135: http://www.x.org/releases/X11R7.7/src/everything/libXvMC-1.0.7.tar.bz2
Source136: http://www.x.org/releases/X11R7.7/src/everything/libXxf86dga-1.1.3.tar.bz2
Source137: http://www.x.org/releases/X11R7.7/src/everything/libXxf86vm-1.1.2.tar.bz2
Source138: http://www.x.org/releases/X11R7.7/src/everything/libfontenc-1.1.1.tar.bz2
Source139: http://www.x.org/releases/X11R7.7/src/everything/libpciaccess-0.13.1.tar.bz2
#Source140: http://www.x.org/releases/X11R7.7/src/everything/libpthread-stubs-0.3.tar.bz2
# libpthread-stubs fails to compile, so we use the same method
# as the el6 libxcb rpm. pthread-stubs.pc.in taken from el6 libxcb rpm
Source140: pthread-stubs.pc.in
Source141: http://www.x.org/releases/X11R7.7/src/everything/libxcb-1.8.1.tar.bz2
Source142: http://www.x.org/releases/X11R7.7/src/everything/libxkbfile-1.0.8.tar.bz2
Source143: http://www.x.org/releases/X11R7.7/src/everything/makedepend-1.0.4.tar.bz2
Source144: http://www.x.org/releases/X11R7.7/src/everything/randrproto-1.3.2.tar.bz2
Source145: http://www.x.org/releases/X11R7.7/src/everything/recordproto-1.14.2.tar.bz2
Source146: http://www.x.org/releases/X11R7.7/src/everything/renderproto-0.11.1.tar.bz2
Source147: http://www.x.org/releases/X11R7.7/src/everything/resourceproto-1.2.0.tar.bz2
Source148: http://www.x.org/releases/X11R7.7/src/everything/scrnsaverproto-1.2.2.tar.bz2
Source149: http://www.x.org/releases/X11R7.7/src/everything/util-macros-1.17.tar.bz2
Source150: http://www.x.org/releases/X11R7.7/src/everything/videoproto-2.3.1.tar.bz2
Source151: http://www.x.org/releases/X11R7.7/src/everything/xcb-proto-1.7.1.tar.bz2
Source152: http://www.x.org/releases/X11R7.7/src/everything/xcmiscproto-1.2.2.tar.bz2
Source153: http://www.x.org/releases/X11R7.7/src/everything/xextproto-7.2.1.tar.bz2
Source154: http://www.x.org/releases/X11R7.7/src/everything/xf86bigfontproto-1.2.0.tar.bz2
Source155: http://www.x.org/releases/X11R7.7/src/everything/xf86dgaproto-2.1.tar.bz2
Source156: http://www.x.org/releases/X11R7.7/src/everything/xf86driproto-2.1.1.tar.bz2
Source157: http://www.x.org/releases/X11R7.7/src/everything/xf86vidmodeproto-2.3.1.tar.bz2
Source158: http://www.x.org/releases/X11R7.7/src/everything/xineramaproto-1.2.1.tar.bz2
Source159: http://www.x.org/releases/X11R7.7/src/everything/xorg-server-1.12.2.tar.bz2
Source160: http://www.x.org/releases/X11R7.7/src/everything/xproto-7.0.23.tar.bz2
Source161: http://www.x.org/releases/X11R7.7/src/everything/xrandr-1.3.5.tar.bz2
Source162: http://www.x.org/releases/X11R7.7/src/everything/xtrans-1.2.7.tar.bz2

Source200: http://fontconfig.org/release/fontconfig-2.8.0.tar.gz
Source201: http://download.savannah.gnu.org/releases/freetype/freetype-old/freetype-2.3.11.tar.bz2
Source202: http://xorg.freedesktop.org/archive/individual/lib/pixman-0.32.4.tar.bz2
Source203: http://dri.freedesktop.org/libdrm/libdrm-2.4.52.tar.bz2
Source204: ftp://ftp.freedesktop.org/pub/mesa/older-versions/9.x/9.2.5/MesaLib-9.2.5.tar.bz2
# NOTE:
#   libgcrypt from el5 is not new enough to satisfy newer Xorg requirements for --with-sha1,
#   which causes Xorg to link against libssl.so and introduce about 10 dynamic dependencies. 
#   to prevent this, build a static libsha1 and link against that.
# NOTE:
Source205: https://github.com/dottedmag/libsha1/archive/0.3.tar.gz

BuildRoot: %{_tmppath}/%{name}-%{version}%{?snap:-%{snap}}-%{release}-root-%(%{__id_u} -n)

# xorg requires newer versions of automake, & autoconf than are available with el5. Use el6 versions.
BuildRequires: automake >= 1.11, autoconf >= 2.60, libtool >= 1.4, gettext >= 0.14.4, gettext-devel >= 0.14.4, bison-devel, python26
BuildRequires: desktop-file-utils, java-devel, jpackage-utils
BuildRequires: pam-devel
>>>>>>> 4c33f2ca86586bb8461526b93cba57a0a14c8baa
BuildRequires: cmake28
BuildRequires: pkgconfig >= 0.20
BuildRequires: gcc44, gcc44-c++
BuildRequires: glibc-devel, libstdc++-devel, libpng-devel
BuildRequires: expat-devel
<<<<<<< HEAD
BuildRequires: gperf, intltool, libtalloc-devel

BuildRequires: openmotif-devel
Requires: openmotif, openmotif22
=======
BuildRequires: git, gperf, intltool, libtalloc-devel
BuildRequires: kernel-headers, libatomic_ops-devel
BuildRequires: xz

>>>>>>> 4c33f2ca86586bb8461526b93cba57a0a14c8baa
Requires(post): initscripts chkconfig coreutils
Requires(postun):coreutils
Requires: hicolor-icon-theme
Requires: tigervnc-license

Provides: vnc = 4.1.3-2, vnc-libs = 4.1.3-2
Obsoletes: vnc < 4.1.3-2, vnc-libs < 4.1.3-2
Provides: tightvnc = 1.5.0-0.15.20090204svn3586
Obsoletes: tightvnc < 1.5.0-0.15.20090204svn3586

<<<<<<< HEAD
Patch4: tigervnc-cookie.patch
Patch10: tigervnc11-ldnow.patch
Patch11: tigervnc11-gethomedir.patch
# https://bugzilla.redhat.com/show_bug.cgi?id=692048
Patch14: tigervnc-x0vncserver-static-libs-fix.patch
Patch15: tigervnc-static-fltk.patch

Patch101: tigervnc-ac-compatibility.patch
Patch102: tigervnc-xorg-1.7.5-remove-copyisolatin1lowered.patch
Patch124: fltk-1.3.2-libdl.patch
Patch125: fltk-1.3.2-static-libs.patch

# Patches from libdrm-2.4.15-4.fc12.src.rpm
# hardcode the 666 instead of 660 for device nodes
Patch133: libdrm-make-dri-perms-okay.patch
# remove backwards compat not needed on Fedora
Patch134: libdrm-2.4.0-no-bc.patch

Patch135: libdrm-page-flip.patch

# nouveau: retry pushbuf ioctl if interrupted by signal
Patch136: libdrm-nouveau-restart-pushbuf.patch
# nouveau: drop rendering on floor rather than asserting if flush fails
Patch137: libdrm-nouveau-drop-rendering.patch
# nouveau: improve reloc API to allow better error handling
Patch138: libdrm-nouveau-better-relocs.patch

# patches from mesa-7.11-5.el6.src.rpm
# ftp://ftp.redhat.com/pub/redhat/linux/enterprise/6Client/en/os/SRPMS/mesa-7.11-5.el6.src.rpm
Patch141: mesa-7.1-osmesa-version.patch
Patch142: mesa-7.1-nukeglthread-debug.patch
Patch143: mesa-no-mach64.patch

#Patch147: mesa-7.1-link-shared.patch
Patch149: intel-revert-vbl.patch
#Patch1410: r600-fix-tfp.patch

#Patch1413: mesa-7.5-sparc64.patch

Patch1430: mesa-7.6-hush-vblank-warning.patch
Patch1431: mesa-7.6-glx13-app-warning.patch

#Patch1440: r300g-no-llvm.patch

# 7.11 branch backport
#Patch1460: mesa-7.11-b9c7773e.patch

# not on 7.11 branch yet
#Patch1470: mesa-7.11-gen6-depth-stalls.patch

#Patch1480: mesa-r600g-new-pciids.patch
#Patch1481: mesa-7.11-ivybridge-server-pci-ids.patch

# Patches from EL6 xorg-x11-server-1.7.7 source RPM
# ftp://ftp.redhat.com/pub/redhat/linux/enterprise/6Client/en/os/SRPMS/xorg-x11-server-1.7.7-29.el6_1.2.src.rpm
Patch5: xserver-1.4.99-pic-libxf86config.patch
Patch6: xserver-1.7.4-z-now.patch

# OpenGL compositing manager feature/optimization patches.
Patch103: xserver-1.5.0-bg-none-root.patch

Patch2014: xserver-1.5.0-projector-fb-size.patch

# Trivial things to never merge upstream ever:
# This really could be done prettier.
Patch5002: xserver-1.4.99-ssh-isnt-local.patch

# force mode debugging on for randr 1.2 drivers
Patch6002: xserver-1.5.1-mode-debug.patch

# don't build the (broken) acpi code
Patch6011: xserver-1.6.0-less-acpi-brokenness.patch

# Make autoconfiguration chose nouveau driver for NVIDIA GPUs
Patch6016: xserver-1.6.1-nouveau.patch

# ajax needs to upstream this
Patch6027: xserver-1.6.0-displayfd.patch
Patch6028: xserver-1.6.99-randr-error-debugging.patch
Patch6030: xserver-1.6.99-right-of.patch
Patch6033: xserver-1.6.99-default-modes.patch
Patch6044: xserver-1.6.99-hush-prerelease-warning.patch
Patch6045: xserver-1.7.0-randr-gamma-restore.patch

Patch6047: xserver-1.7.0-glx-versioning.patch
#Patch6048: xserver-1.7.0-exa-fix-mixed.patch
Patch6049: xserver-1.7.1-multilib.patch
Patch6051: xserver-1.7.1-gamma-kdm-fix.patch
Patch6052: xserver-1.7.1-libcrypto.patch
Patch6066: xserver-1.7.1-glx14-swrast.patch

Patch6067: xserver-1.7.7-exa-master.patch

Patch6070: xserver-1.7.3-no-free-on-abort.patch
# 558613
Patch6075: xserver-1.7.4-qxl-autoconfig.patch
# 516918
Patch6076: xserver-1.7.4-dpms-timeouts.patch
Patch6077: xserver-1.7.6-export-dix-functions.patch
Patch6078: xserver-1.7.6-export-more-dix-functions.patch

# 583544 - Pointer jumps to lower-right corner when clicking mousekeys
Patch6087: xserver-1.7.6-pointerkeys.patch

Patch7002: xserver-1.7.6-no-connected-outputs.patch
# 586926 - randr change while off vt
Patch7003: xserver-1.7.6-randr-vt-switch.patch
# 582710 - pam support
Patch7004: xserver-1.1.1-pam.patch
# 584927 - xinerama coordinate sign fix
Patch7005: xserver-1.7.6-deviceevent-coordinates-xinerama.patch
# 585371 - default mode list unification
Patch7006: xserver-1.7.6-default-modes.patch
# 586567 - big window crash when try to resize
Patch7007: xserver-1.7.7-compresize-fix.patch
# 602080 - fix unnecessary fb resize in multi-head configurations
Patch7008: xserver-1.7.7-randr-initial.patch
# 600180  - Buffer overflow in XKB geometry copying code.
Patch7009: xserver-1.7.7-xkb-invalid-writes.patch
# 600116  - Properties are not reset in the second server generation
Patch7010: xserver-1.7.7-property-generation-reset.patch
# 594523  - Wrong axis mode for absolute axes 
Patch7011: xserver-1.7.7-device-mode-list.patch
# 602511  - Stuck modifiers when using multiple keyboards or XTEST
Patch7012: xserver-1.7.7-modifier-keycount.patch
# 588640  - XKEYBOARD Warning: Duplicate shape name ""
Patch7013: xserver-1.7.7-xkb-geom-copy.patch
# 574486 - Dual head setup overlaps one pixel 
Patch7014: xserver-1.7.7-fix-randr-rotation.patch
# 600505 - Xephyr utility should be resizeable
Patch7015: xserver-1.7.7-make-ephyr-resize.patch
# 604057 - fix aspect match for classic drivers
Patch7016: xserver-1.7.7-improve-mode-selection.patch
# 607045 - DGA client can crash the server
Patch7017: xserver-1.7.7-dga-master-keyboard.patch
# 607410 - Reproducible stuck grab on server
Patch7018: xserver-1.7.7-event-mask-revert.patch
# 607051 - Keyboard bell settings don't apply to keyboards.
Patch7019: xserver-1.7.7-sd-keyboard-controls.patch
# 607022 - segfault during Xorg -showopts
Patch7020: xserver-1.7.7-showopts-segv.patch
# Related 607150
Patch7021: xserver-1.7.7-xkb-purge-includes.patch
# Related 607150
Patch7022: xserver-1.7.7-xkb-rename-fakebutton.patch
# Related 607150
Patch7023: xserver-1.7.7-xkb-pointerkeys-on-master.patch
# 607150 - Mouse button never releases when xkb PointerKeys are used
Patch7024: xserver-1.7.7-xkb-lockedPtrBtns-state-merge.patch
# 607150 - Mouse button never releases when xkb PointerKeys are used, part2
Patch7025: xserver-1.7.7-release-xtest-on-phys-buttons.patch
# 581505 - Xephyr crashes inside kvm-qemu virtual host
Patch7026: xserver-1.7.7-xephyr-24bpp.patch
# 605302 - vesa doesn't work on intel gen6
Patch7027: xserver-1.7.7-int10-reserved-areas.patch
# 618422 - Wrong handling of devices with more than 2 valuators
Patch7028: xserver-1.7.7-postfix-DCE-PointerKeys.patch
# related 618422, Patch7028
Patch7029: xserver-1.7.7-reset-unused-classes.patch
# 601319 - LVDS activated when notebook lid is closed
Patch7030: xserver-1.7.7-lid-hack.patch
# 585283 - xrandr allows mouse to move into non-existant screen locations
Patch7031: xserver-1.7.7-randr-cursor-dead-zones.patch
# 620333 - mga shows blank screen when X server starts
Patch7032: xserver-1.7.7-ddc-probe-less.patch
# 638234 - Bump classic driver default resolution to 1024x768
Patch7033: xserver-1.7.7-classic-default-mode.patch

Patch8000: cve-2011-4818.patch
Patch8001: cve-2011-4818-extra.patch

# Add -lm when linking X demos
Patch9020: freetype-2.1.10-enable-ft2-bci.patch
Patch9021: freetype-2.3.0-enable-spr.patch

# Enable otvalid and gxvalid modules
Patch9046: freetype-2.2.1-enable-valid.patch

# Fix multilib conflicts
Patch9088: freetype-multilib.patch

Patch9089: freetype-2.3.11-CVE-2010-2498.patch
Patch9090: freetype-2.3.11-CVE-2010-2499.patch
Patch9091: freetype-2.3.11-CVE-2010-2500.patch
Patch9092: freetype-2.3.11-CVE-2010-2519.patch
Patch9093: freetype-2.3.11-CVE-2010-2520.patch
#Patch9094: freetype-2.3.11-CVE-2010-2527.patch
#Patch9095: freetype-2.3.11-axis-name-overflow.patch
Patch9096: freetype-2.3.11-CVE-2010-1797.patch
Patch9097: freetype-2.3.11-CVE-2010-2805.patch
Patch9098: freetype-2.3.11-CVE-2010-2806.patch
Patch9099: freetype-2.3.11-CVE-2010-2808.patch
Patch9100: freetype-2.3.11-CVE-2010-3311.patch
Patch9101: freetype-2.3.11-CVE-2010-3855.patch
Patch9102: freetype-2.3.11-CVE-2011-0226.patch
Patch9103: freetype-2.3.11-CVE-2011-3256.patch
Patch9104: freetype-2.3.11-CVE-2011-3439.patch
Patch9105: freetype-2.3.11-CVE-2012-1126.patch
Patch9106: freetype-2.3.11-CVE-2012-1127.patch
Patch9107: freetype-2.3.11-CVE-2012-1130.patch
Patch9108: freetype-2.3.11-CVE-2012-1131.patch
Patch9109: freetype-2.3.11-CVE-2012-1132.patch
Patch9110: freetype-2.3.11-CVE-2012-1134.patch
Patch9111: freetype-2.3.11-CVE-2012-1136.patch
Patch9112: freetype-2.3.11-CVE-2012-1137.patch
Patch9113: freetype-2.3.11-CVE-2012-1139.patch
Patch9114: freetype-2.3.11-CVE-2012-1140.patch
Patch9115: freetype-2.3.11-CVE-2012-1141.patch
Patch9116: freetype-2.3.11-CVE-2012-1142.patch
Patch9117: freetype-2.3.11-CVE-2012-1143.patch
Patch9118: freetype-2.3.11-CVE-2012-1144.patch
Patch9119: freetype-2.3.11-bdf-overflow.patch
Patch9120: freetype-2.3.11-array-initialization.patch

Patch10001: xtrans-1.0.3-avoid-gethostname.patch

Patch10102: dont-forward-keycode-0.patch
Patch10103: libX11-1.3.1-creategc-man-page.patch

Patch10201: libXext-1.1-XAllocID.patch

Patch10301: libfontenc-1.0.0-get-fontdir-from-pkgconfig.patch

Patch10400: libXt-1.0.2-libsm-fix.patch
=======
# tigervnc patches
Patch4: tigervnc-cookie.patch
Patch12: tigervnc14-static-build-fixes.patch

# fltk patches
Patch15: fltk-1.3.3-static-libs.patch

# freetype patches
Patch20:  freetype-2.1.10-enable-ft2-bci.patch
Patch21:  freetype-2.3.0-enable-spr.patch

# Enable otvalid and gxvalid modules
Patch46:  freetype-2.2.1-enable-valid.patch

# Fix multilib conflicts
Patch88:  freetype-multilib.patch

Patch89:  freetype-2.3.11-CVE-2010-2498.patch
Patch90:  freetype-2.3.11-CVE-2010-2499.patch
Patch91:  freetype-2.3.11-CVE-2010-2500.patch
Patch92:  freetype-2.3.11-CVE-2010-2519.patch
Patch93:  freetype-2.3.11-CVE-2010-2520.patch
Patch96:  freetype-2.3.11-CVE-2010-1797.patch
Patch97:  freetype-2.3.11-CVE-2010-2805.patch
Patch98:  freetype-2.3.11-CVE-2010-2806.patch
Patch99:  freetype-2.3.11-CVE-2010-2808.patch
Patch100:  freetype-2.3.11-CVE-2010-3311.patch
Patch101:  freetype-2.3.11-CVE-2010-3855.patch
Patch102:  freetype-2.3.11-CVE-2011-0226.patch
Patch103:  freetype-2.3.11-CVE-2011-3256.patch
Patch104:  freetype-2.3.11-CVE-2011-3439.patch
Patch105:  freetype-2.3.11-CVE-2012-1126.patch
Patch106:  freetype-2.3.11-CVE-2012-1127.patch
Patch107:  freetype-2.3.11-CVE-2012-1130.patch
Patch108:  freetype-2.3.11-CVE-2012-1131.patch
Patch109:  freetype-2.3.11-CVE-2012-1132.patch
Patch110:  freetype-2.3.11-CVE-2012-1134.patch
Patch111:  freetype-2.3.11-CVE-2012-1136.patch
Patch112:  freetype-2.3.11-CVE-2012-1137.patch
Patch113:  freetype-2.3.11-CVE-2012-1139.patch
Patch114:  freetype-2.3.11-CVE-2012-1140.patch
Patch115:  freetype-2.3.11-CVE-2012-1141.patch
Patch116:  freetype-2.3.11-CVE-2012-1142.patch
Patch117:  freetype-2.3.11-CVE-2012-1143.patch
Patch118:  freetype-2.3.11-CVE-2012-1144.patch
Patch119:  freetype-2.3.11-bdf-overflow.patch
Patch120:  freetype-2.3.11-array-initialization.patch
Patch121:  freetype-2.3.11-CVE-2012-5669.patch

# Patches for Xorg CVE-2014-12-09 taken from Debian:
# https://release.debian.org/proposed-updates/stable_diffs/xorg-server_1.12.4-6+deb7u5.debdiff
Patch10000: 16_CVE-2014-mult.diff
Patch10001: 17_CVE-regressions.diff
>>>>>>> 4c33f2ca86586bb8461526b93cba57a0a14c8baa

%description
Virtual Network Computing (VNC) is a remote display system which
allows you to view a computing 'desktop' environment not only on the
machine where it is running, but from anywhere on the Internet and
from a wide variety of machine architectures.  This package contains a
client which will allow you to connect to other desktops running a VNC
server.

%package server
Summary: A TigerVNC server
Group: User Interface/X
Provides: vnc-server = 4.1.3-2, vnc-libs = 4.1.3-2
Obsoletes: vnc-server < 4.1.3-2, vnc-libs < 4.1.3-2
Provides: tightvnc-server = 1.5.0-0.15.20090204svn3586
Obsoletes: tightvnc-server < 1.5.0-0.15.20090204svn3586
Requires: perl
Requires: tigervnc-server-minimal
Requires: xorg-x11-xauth

%description server
The VNC system allows you to access the same desktop from a wide
variety of platforms.  This package includes set of utilities
which make usage of TigerVNC server more user friendly. It also
contains x0vncserver program which can export your active
X session.

%package server-minimal
Summary: A minimal installation of TigerVNC server
Group: User Interface/X
Requires(post): chkconfig
Requires(preun):chkconfig
Requires(preun):initscripts
Requires(postun):initscripts

Requires: xkeyboard-config, xorg-x11-xkb-utils
<<<<<<< HEAD
=======
Requires: keyutils-libs-devel
>>>>>>> 4c33f2ca86586bb8461526b93cba57a0a14c8baa
Requires: tigervnc-license

%description server-minimal
The VNC system allows you to access the same desktop from a wide
variety of platforms. This package contains minimal installation
of TigerVNC server, allowing others to access the desktop on your
machine.

%package server-applet
Summary: Java TigerVNC viewer applet for TigerVNC server
Group: User Interface/X
Requires: tigervnc-server, java, jpackage-utils
%if 0%{?fedora} >= 10 || 0%{?rhel} >= 6 || 0%{?centos} >= 6
BuildArch: noarch
%endif

%description server-applet
The Java TigerVNC viewer applet for web browsers. Install this package to allow
clients to use web browser when connect to the TigerVNC server.

%package license
Summary: License of TigerVNC suite
Group: User Interface/X
%if 0%{?fedora} >= 10 || 0%{?rhel} >= 6 || 0%{?centos} >= 6
BuildArch: noarch
%endif

%description license
This package contains license of the TigerVNC suite

%package icons
Summary: Icons for TigerVNC viewer
Group: User Interface/X
%if 0%{?fedora} >= 10 || 0%{?rhel} >= 6 || 0%{?centos} >= 6
BuildArch: noarch
%endif

%description icons
This package contains icons for TigerVNC viewer

%prep
rm -rf %{_builddir}/%{name}-%{version}%{?snap:-%{snap}}
%setup -q -n %{name}-%{version}%{?snap:-%{snap}}

<<<<<<< HEAD
# sed -i -e 's/80/0/g' CMakeLists.txt
cp %SOURCE9 cmake/Modules/
%patch4 -p1 -b .cookie
%patch10 -p1 -b .ldnow
%patch11 -p1 -b .gethomedir
%patch15 -p1 -b .static-fltk
%patch14 -p1 -b .x0vncserver

tar xzf %SOURCE11
pushd fltk-*
for p in `find ../contrib/fltk -maxdepth 1 -type f -name "*.patch"|sort` ;
do
  patch -p1 -i $p
done
cp %SOURCE9 CMake/
%patch124 -p1 -b .libdl
%patch125 -p1 -b .static-libs
popd

tar xzf %SOURCE12

mkdir xorg
pushd xorg
tar xjf %SOURCE98
tar xjf %SOURCE99
=======
# Search paths for X11 are hard coded into FindX11.cmake
cp %SOURCE9 cmake/Modules/
sed -i -e "s#@_includedir@#%{xorg_buildroot}%{_includedir}#" cmake/Modules/FindX11.cmake
sed -i -e "s#@_libdir@#%{xorg_buildroot}%{_libdir}#" cmake/Modules/FindX11.cmake
%patch4 -p1 -b .cookie
%patch12 -p1 -b .static-build-fixes

tar xzf %SOURCE11
pushd fltk-*
%patch15 -p1 -b .static-libs
popd

tar xzf %SOURCE12
tar xjf %SOURCE13
tar xjf %SOURCE14
tar xzf %SOURCE15
tar xzf %SOURCE16
xzcat %SOURCE17 | tar xf -

mkdir xorg
pushd xorg
>>>>>>> 4c33f2ca86586bb8461526b93cba57a0a14c8baa
tar xjf %SOURCE100
tar xjf %SOURCE101
tar xjf %SOURCE102
tar xjf %SOURCE103
tar xjf %SOURCE104
tar xjf %SOURCE105
tar xjf %SOURCE106
tar xjf %SOURCE107
tar xjf %SOURCE108
tar xjf %SOURCE109
tar xjf %SOURCE110
tar xjf %SOURCE111
tar xjf %SOURCE112
tar xjf %SOURCE113
tar xjf %SOURCE114
tar xjf %SOURCE115
tar xjf %SOURCE116
tar xjf %SOURCE117
tar xjf %SOURCE118
tar xjf %SOURCE119
tar xjf %SOURCE120
tar xjf %SOURCE121
tar xjf %SOURCE122
tar xjf %SOURCE123
tar xjf %SOURCE124
tar xjf %SOURCE125
tar xjf %SOURCE126
tar xjf %SOURCE127
tar xjf %SOURCE128
tar xjf %SOURCE129
tar xjf %SOURCE130
tar xjf %SOURCE131
tar xjf %SOURCE132
tar xjf %SOURCE133
tar xjf %SOURCE134
tar xjf %SOURCE135
tar xjf %SOURCE136
tar xjf %SOURCE137
tar xjf %SOURCE138
tar xjf %SOURCE139
<<<<<<< HEAD
tar xjf %SOURCE140
=======

>>>>>>> 4c33f2ca86586bb8461526b93cba57a0a14c8baa
tar xjf %SOURCE141
tar xjf %SOURCE142
tar xjf %SOURCE143
tar xjf %SOURCE144
tar xjf %SOURCE145
tar xjf %SOURCE146
tar xjf %SOURCE147
tar xjf %SOURCE148
tar xjf %SOURCE149
tar xjf %SOURCE150
tar xjf %SOURCE151
tar xjf %SOURCE152
tar xjf %SOURCE153
tar xjf %SOURCE154
tar xjf %SOURCE155
tar xjf %SOURCE156
<<<<<<< HEAD
# tar xjf %SOURCE157
# tar xjf %SOURCE158
tar xjf %SOURCE159
tar xjf %SOURCE160
tar xjf %SOURCE161
tar xzf %SOURCE162
tar xjf %SOURCE163
tar xjf %SOURCE164
popd
tar xzf %SOURCE200
cp -a xorg/xorg-server-1.*/* unix/xserver
pushd xorg
pushd libdrm-*
%patch133 -p1 -b .forceperms
%patch134 -p1 -b .no-bc
%patch135 -p1 -b .page-flip
%patch136 -p1 -b .nouveau-pbrestart
%patch137 -p1 -b .nouveau-drop
%patch138 -p1 -b .nouveau-relocs
popd
pushd Mesa-*
%patch141 -p1 -b .osmesa
%patch142 -p1 -b .intel-glthread
%patch143 -p1 -b .no-mach64
#%patch147 -p1 -b .dricore
%patch149 -p1 -b .intel-vbl
#%patch1410 -p1 -b .r600_tfp
#%patch1413 -p1 -b .sparc64
%patch1430 -p1 -b .vblank-warning
%patch1431 -p1 -b .glx13-warning
#%patch1440 -p1 -b .r300g
#%patch1460 -p1

#%patch1470 -p1 -b .depth-stall

#%patch1480 -p1 -b .r600gpciids
#%patch1481 -p1 -b .ivbpciid
popd

pushd freetype-*
%patch9020 -p1 -b .enable-ft2-bci
%patch9021 -p1 -b .enable-spr

# Enable otvalid and gxvalid modules
%patch9046 -p1 -b .enable-valid

# Fix multilib conflicts
%patch9088 -p1 -b .multilib

%patch9089 -p1 -b .CVE-2010-2498
%patch9090 -p1 -b .CVE-2010-2499
%patch9091 -p1 -b .CVE-2010-2500
%patch9092 -p1 -b .CVE-2010-2519
%patch9093 -p1 -b .CVE-2010-2520
%patch9096 -p1 -b .CVE-2010-1797
%patch9097 -p1 -b .CVE-2010-2805
%patch9098 -p1 -b .CVE-2010-2806
%patch9099 -p1 -b .CVE-2010-2808
%patch9100 -p1 -b .CVE-2010-3311
%patch9101 -p1 -b .CVE-2010-3855
%patch9102 -p1 -b .CVE-2011-0226
%patch9103 -p1 -b .CVE-2011-3256
%patch9104 -p1 -b .CVE-2011-3439
%patch9105 -p1 -b .CVE-2012-1126
%patch9106 -p1 -b .CVE-2012-1127
%patch9107 -p1 -b .CVE-2012-1130
%patch9108 -p1 -b .CVE-2012-1131
%patch9109 -p1 -b .CVE-2012-1132
%patch9110 -p1 -b .CVE-2012-1134
%patch9111 -p1 -b .CVE-2012-1136
%patch9112 -p1 -b .CVE-2012-1137
%patch9113 -p1 -b .CVE-2012-1139
%patch9114 -p1 -b .CVE-2012-1140
%patch9115 -p1 -b .CVE-2012-1141
%patch9116 -p1 -b .CVE-2012-1142
%patch9117 -p1 -b .CVE-2012-1143
%patch9118 -p1 -b .CVE-2012-1144
%patch9119 -p1 -b .bdf-overflow
%patch9120 -p1 -b .array-initialization
popd

pushd xtrans-*
%patch10001 -p1 -b .my-name-is-unix
popd

pushd libX11-*
%patch10102 -p1 -b .dont-forward-keycode-0
%patch10103 -p1 -b .manual
popd

pushd libXext-*
%patch10201 -p1 
popd

pushd libfontenc-*
%patch10301 -p0 -b .get-fontdir-from-pkgconfig
popd

pushd libXt-*
%patch10400 -p1 -b .libsm-fix
popd

popd

pushd unix/xserver
patch -p1 < %{_builddir}/%{name}-%{version}%{?snap:-%{snap}}/unix/xserver17.patch
for all in `find %{_builddir}/%{name}-%{version}%{?snap:-%{snap}}/unix/xorg-7.5-patches/ -type f |grep '.*\.patch$'`; do
	echo Applying $all
	patch -p1 < $all
done
%patch101 -p1 -b .ac-compatibility
%patch102 -p1 -b .CopyISOLatin1Lowered

%patch5 -p1 -b .xserver-1.4.99-pic-libxf86config
%patch6 -p1 -b .xserver-1.7.4-z-now

# OpenGL compositing manager feature/optimization patches.
%patch103 -p1 -b .xserver-1.5.0-bg-none-root

%patch2014 -p1 -b .xserver-1.5.0-projector-fb-size

# Trivial things to never merge upstream ever:
# This really could be done prettier.
%patch5002 -p1 -b .xserver-1.4.99-ssh-isnt-local

# force mode debugging on for randr 1.2 drivers
%patch6002 -p1 -b .xserver-1.5.1-mode-debug

# don't build the (broken) acpi code
%patch6011 -p1 -b .xserver-1.6.0-less-acpi-brokenness

# Make autoconfiguration chose nouveau driver for NVIDIA GPUs
%patch6016 -p1 -b .xserver-1.6.1-nouveau

# ajax needs to upstream this
%patch6027 -p1 -b .xserver-1.6.0-displayfd
%patch6028 -p1 -b .xserver-1.6.99-randr-error-debugging
%patch6030 -p1 -b .xserver-1.6.99-right-of
%patch6033 -p1 -b .xserver-1.6.99-default-modes
%patch6044 -p1 -b .xserver-1.6.99-hush-prerelease-warning
%patch6045 -p1 -b .xserver-1.7.0-randr-gamma-restore

%patch6047 -p1 -b .xserver-1.7.0-glx-versioning
#%patch6048 -p1 -b .xserver-1.7.0-exa-fix-mixed
%patch6049 -p1 -b .xserver-1.7.1-multilib
%patch6051 -p1 -b .xserver-1.7.1-gamma-kdm-fix
%patch6052 -p1 -b .xserver-1.7.1-libcrypto
%patch6066 -p1 -b .xserver-1.7.1-glx14-swrast

%patch6067 -p1 -b .xserver-1.7.7-exa-master

%patch6070 -p1 -b .xserver-1.7.3-no-free-on-abort
# 558613
%patch6075 -p1 -b .xserver-1.7.4-qxl-autoconfig
# 516918
%patch6076 -p1 -b .xserver-1.7.4-dpms-timeouts
%patch6077 -p1 -b .xserver-1.7.6-export-dix-functions
%patch6078 -p1 -b .xserver-1.7.6-export-more-dix-functions

# 583544 - Pointer jumps to lower-right corner when clicking mousekeys
%patch6087 -p1 -b .xserver-1.7.6-pointerkeys

%patch7002 -p1 -b .xserver-1.7.6-no-connected-outputs
# 586926 - randr change while off vt
%patch7003 -p1 -b .xserver-1.7.6-randr-vt-switch
# 582710 - pam support
%patch7004 -p1 -b .xserver-1.1.1-pam
# 584927 - xinerama coordinate sign fix
%patch7005 -p1 -b .xserver-1.7.6-deviceevent-coordinates-xinerama
# 585371 - default mode list unification
%patch7006 -p1 -b .xserver-1.7.6-default-modes
# 586567 - big window crash when try to resize
%patch7007 -p1 -b .xserver-1.7.7-compresize-fix
# 602080 - fix unnecessary fb resize in multi-head configurations
%patch7008 -p1 -b .xserver-1.7.7-randr-initial
# 600180 - Buffer overflow in XKB geometry copying code.
%patch7009 -p1 -b .xserver-1.7.7-xkb-invalid-writes
# 600116 - Properties are not reset in the second server generation
%patch7010 -p1 -b .xserver-1.7.7-property-generation-reset
# 594523 - Wrong axis mode for absolute axes 
%patch7011 -p1 -b .xserver-1.7.7-device-mode-list
# 602511 - Stuck modifiers when using multiple keyboards or XTEST
%patch7012 -p1 -b .xserver-1.7.7-modifier-keycount
# 588640 - XKEYBOARD Warning: Duplicate shape name ""
%patch7013 -p1 -b .xserver-1.7.7-xkb-geom-copy
# 574486 - Dual head setup overlaps one pixel 
%patch7014 -p1 -b .xserver-1.7.7-fix-randr-rotation
# 600505 - Xephyr utility should be resizeable
%patch7015 -p1 -b .xserver-1.7.7-make-ephyr-resize
# 604057 - fix aspect match for classic drivers
%patch7016 -p1 -b .xserver-1.7.7-improve-mode-selection
# 607045 - DGA client can crash the server
%patch7017 -p1 -b .xserver-1.7.7-dga-master-keyboard
# 607410 - Reproducible stuck grab on server
%patch7018 -p1 -b .xserver-1.7.7-event-mask-revert
# 607051 - Keyboard bell settings don't apply to keyboards.
%patch7019 -p1 -b .xserver-1.7.7-sd-keyboard-controls
# 607022 - segfault during Xorg -showopts
%patch7020 -p1 -b .xserver-1.7.7-showopts-segv
# Related 607150
%patch7021 -p1 -b .xserver-1.7.7-xkb-purge-includes
# Related 607150
%patch7022 -p1 -b .xserver-1.7.7-xkb-rename-fakebutton
# Related 607150
%patch7023 -p1 -b .xserver-1.7.7-xkb-pointerkeys-on-master
# 607150 - Mouse button never releases when xkb PointerKeys are used
%patch7024 -p1 -b .xserver-1.7.7-xkb-lockedPtrBtns-state-merge
# 607150 - Mouse button never releases when xkb PointerKeys are used, part2
%patch7025 -p1 -b .xserver-1.7.7-release-xtest-on-phys-buttons
# 581505 - Xephyr crashes inside kvm-qemu virtual host
%patch7026 -p1 -b .xserver-1.7.7-xephyr-24bpp
# 605302 - vesa doesn't work on intel gen6
%patch7027 -p1 -b .xserver-1.7.7-int10-reserved-areas
# 618422 - Wrong handling of devices with more than 2 valuators
%patch7028 -p1 -b .xserver-1.7.7-postfix-DCE-PointerKeys
# related 618422, Patch7028
%patch7029 -p1 -b .xserver-1.7.7-reset-unused-classes
# 601319 - LVDS activated when notebook lid is closed
%patch7030 -p1 -b .xserver-1.7.7-lid-hack
# 585283 - xrandr allows mouse to move into non-existant screen locations
%patch7031 -p1 -b .xserver-1.7.7-randr-cursor-dead-zones
# 620333 - mga shows blank screen when X server starts
%patch7032 -p1 -b .xserver-1.7.7-ddc-probe-less
# 638234 - Bump classic driver default resolution to 1024x768
%patch7033 -p1 -b .xserver-1.7.7-classic-default-mode

%patch8000 -p1 -b .cve-2011-4818
%patch8001 -p1 -b .cve-2011-4818-extra
=======
tar xjf %SOURCE157
tar xjf %SOURCE158
tar xjf %SOURCE159
tar xjf %SOURCE160
tar xjf %SOURCE161
tar xjf %SOURCE162
tar xzf %SOURCE200
tar xjf %SOURCE201
pushd freetype-*
%patch46  -p1 -b .enable-valid
%patch88 -p1 -b .multilib
%patch89 -p1 -b .CVE-2010-2498
%patch90 -p1 -b .CVE-2010-2499
%patch91 -p1 -b .CVE-2010-2500
%patch92 -p1 -b .CVE-2010-2519
%patch93 -p1 -b .CVE-2010-2520
%patch96 -p1 -b .CVE-2010-1797
%patch97 -p1 -b .CVE-2010-2805
%patch98 -p1 -b .CVE-2010-2806
%patch99 -p1 -b .CVE-2010-2808
%patch100 -p1 -b .CVE-2010-3311
%patch101 -p1 -b .CVE-2010-3855
%patch102 -p1 -b .CVE-2011-0226
%patch103 -p1 -b .CVE-2011-3256
%patch104 -p1 -b .CVE-2011-3439
%patch105 -p1 -b .CVE-2012-1126
%patch106 -p1 -b .CVE-2012-1127
%patch107 -p1 -b .CVE-2012-1130
%patch108 -p1 -b .CVE-2012-1131
%patch109 -p1 -b .CVE-2012-1132
%patch110 -p1 -b .CVE-2012-1134
%patch111 -p1 -b .CVE-2012-1136
%patch112 -p1 -b .CVE-2012-1137
%patch113 -p1 -b .CVE-2012-1139
%patch114 -p1 -b .CVE-2012-1140
%patch115 -p1 -b .CVE-2012-1141
%patch116 -p1 -b .CVE-2012-1142
%patch117 -p1 -b .CVE-2012-1143
%patch118 -p1 -b .CVE-2012-1144
%patch119 -p1 -b .bdf-overflow
%patch120 -p1 -b .array-initialization
%patch121 -p1 -b .CVE-2012-5669
popd
tar xjf %SOURCE202
tar xjf %SOURCE203
tar xjf %SOURCE204
pushd xorg-server-1*
%patch10000 -p1 -b .CVE-2014-mult
%patch10001 -p1 -b .CVE-regressions
for f in `find . -type f -perm -000`; do
  chmod +r "$f"
done
popd
tar xzf %SOURCE205
popd

cp -a xorg/xorg-server-1*/* unix/xserver

pushd unix/xserver
for all in `find . -type f -perm -001`; do
  chmod -x "$all"
done
patch -p1 < %{_builddir}/%{name}-%{version}%{?snap:-%{snap}}/unix/xserver112.patch
>>>>>>> 4c33f2ca86586bb8461526b93cba57a0a14c8baa

popd

%build
<<<<<<< HEAD
%define tigervnc_src_dir %{_builddir}/%{name}-%{version}%{?snap:-%{snap}}
%define static_lib_buildroot %{tigervnc_src_dir}/build
=======
>>>>>>> 4c33f2ca86586bb8461526b93cba57a0a14c8baa
export CC=gcc44
export CXX=g++44
export CFLAGS="$RPM_OPT_FLAGS -fPIC"
export CXXFLAGS="$CFLAGS -static-libgcc"
<<<<<<< HEAD

%define xorg_buildroot %{tigervnc_src_dir}/xorg.build
mkdir -p %{xorg_buildroot}%{_libdir}
pushd %{xorg_buildroot}%{_libdir}
ln -s `g++44 -print-file-name=libexpat.a`
ln -s `g++44 -print-file-name=libgcrypt.a`
ln -s `g++44 -print-file-name=libgpg-error.a`
ln -s `g++44 -print-file-name=libgnutls.a`
ln -s `g++44 -print-file-name=libstdc++.a`
ln -s `g++44 -print-file-name=libcrypto.a`
ln -s `g++44 -print-file-name=libz.a`
ln -s `g++44 -print-file-name=libgcc.a`
ln -s `g++44 -print-file-name=libpng.a`
=======
export PYTHON=python26

mkdir -p %{xorg_buildroot}%{_libdir}
pushd %{xorg_buildroot}%{_libdir}
ln -s `g++44 -print-file-name=libz.a`
ln -s `g++44 -print-file-name=libgcc.a`
ln -s `g++44 -print-file-name=libexpat.a`
ln -s `g++44 -print-file-name=libcrypto.a`
>>>>>>> 4c33f2ca86586bb8461526b93cba57a0a14c8baa
popd

echo "*** Building libjpeg-turbo ***"
pushd libjpeg-turbo-*
<<<<<<< HEAD
./configure --prefix=%{_prefix} --libdir=%{_libdir} --disable-nls --enable-static --disable-shared
make %{?_smp_mflags} DESTDIR=%{xorg_buildroot} install
=======
LDFLAGS="$LDFLAGS -static" PKG_CONFIG="pkg-config --static" ./configure --prefix=%{_prefix} --libdir=%{_libdir} --disable-nls --enable-static --disable-shared
make %{?_smp_mflags} DESTDIR=%{xorg_buildroot} install
popd

echo "*** Building Xorg ***"
pushd xorg

echo "*** Building libsha1 ***"
pushd libsha1-*
autoreconf -fiv
LDFLAGS="$LDFLAGS -static" PKG_CONFIG="pkg-config --static" ./configure --prefix=%{_prefix} --libdir=%{_libdir} --disable-nls --enable-static --disable-shared
make %{?_smp_mflags} DESTDIR=%{xorg_buildroot} install
find %{xorg_buildroot}%{_prefix} -type f -name "*.la" -delete
find %{xorg_buildroot}%{_prefix} -type f -name "*.pc" -exec sed -i -e "s|libdir=%{_libdir}|libdir=%{xorg_buildroot}%{_libdir}|" {} \;
find %{xorg_buildroot}%{_prefix} -type f -name "*.pc" -exec sed -i -e "s|prefix=%{_prefix}|prefix=%{xorg_buildroot}%{_prefix}|" {} \;
popd
>>>>>>> 4c33f2ca86586bb8461526b93cba57a0a14c8baa
popd

export CFLAGS="$RPM_OPT_FLAGS -fPIC -I%{xorg_buildroot}%{_includedir}"
export CXXFLAGS="$RPM_OPT_FLAGS -fPIC -I%{xorg_buildroot}%{_includedir} -static-libgcc"
export CPPFLAGS=$CXXFLAGS
<<<<<<< HEAD
export LDFLAGS="$LDFLAGS -L%{xorg_buildroot}%{_libdir}"
export ACLOCAL="aclocal -I %{xorg_buildroot}%{_datadir}/aclocal"
export PKG_CONFIG_PATH="%{xorg_buildroot}%{_libdir}/pkgconfig:%{xorg_buildroot}%{_datadir}/pkgconfig"

echo "*** Building Xorg ***"
=======
export LDFLAGS="-L%{xorg_buildroot}%{_libdir} -L%{xorg_buildroot}%{_libdir}/tigervnc $LDFLAGS"
export ACLOCAL="aclocal -I %{xorg_buildroot}%{_datadir}/aclocal"
export PKG_CONFIG_PATH="%{xorg_buildroot}%{_libdir}/pkgconfig:%{xorg_buildroot}%{_libdir}/tigervnc/pkgconfig:%{xorg_buildroot}%{_datadir}/pkgconfig:%{_libdir}/pkgconfig:%{_datadir}/pkgconfig"

echo "*** Building gmp ***"
pushd gmp-*
%ifarch x86_64 s390x ia64 ppc64 alpha sparc64
LDFLAGS="$LDFLAGS -static" PKG_CONFIG="pkg-config --static" ABI=64 ./configure --prefix=%{_prefix} --libdir=%{_libdir} --enable-static --disable-shared --enable-cxx
%else
LDFLAGS="$LDFLAGS -static" PKG_CONFIG="pkg-config --static" ABI=32 ./configure --prefix=%{_prefix} --libdir=%{_libdir} --enable-static --disable-shared --enable-cxx
%endif
make %{?_smp_mflags} DESTDIR=%{xorg_buildroot} install
find %{xorg_buildroot}%{_prefix} -type f -name "*.la" -delete
find %{xorg_buildroot}%{_prefix} -type f -name "*.pc" -exec sed -i -e "s|libdir=%{_libdir}|libdir=%{xorg_buildroot}%{_libdir}|" {} \;
find %{xorg_buildroot}%{_prefix} -type f -name "*.pc" -exec sed -i -e "s|prefix=%{_prefix}|prefix=%{xorg_buildroot}%{_prefix}|" {} \;
popd

echo "*** Building libtasn1 ***"
pushd libtasn1-*
LDFLAGS="$LDFLAGS -static" PKG_CONFIG="pkg-config --static" ./configure --prefix=%{_prefix} --libdir=%{_libdir} --enable-static --disable-shared
make %{?_smp_mflags} DESTDIR=%{xorg_buildroot} install
find %{xorg_buildroot}%{_prefix} -type f -name "*.la" -delete
find %{xorg_buildroot}%{_prefix} -type f -name "*.pc" -exec sed -i -e "s|libdir=%{_libdir}|libdir=%{xorg_buildroot}%{_libdir}|" {} \;
find %{xorg_buildroot}%{_prefix} -type f -name "*.pc" -exec sed -i -e "s|prefix=%{_prefix}|prefix=%{xorg_buildroot}%{_prefix}|" {} \;
popd

echo "*** Building nettle ***"
pushd nettle-*
autoreconf -fiv
LDFLAGS="$LDFLAGS -static" PKG_CONFIG="pkg-config --static" ./configure --prefix=%{_prefix} --libdir=%{_libdir} --enable-static --disable-shared --disable-openssl
make %{?_smp_mflags} DESTDIR=%{xorg_buildroot} install
find %{xorg_buildroot}%{_prefix} -type f -name "*.la" -delete
find %{xorg_buildroot}%{_prefix} -type f -name "*.pc" -exec sed -i -e "s|libdir=%{_libdir}|libdir=%{xorg_buildroot}%{_libdir}|" {} \;
find %{xorg_buildroot}%{_prefix} -type f -name "*.pc" -exec sed -i -e "s|prefix=%{_prefix}|prefix=%{xorg_buildroot}%{_prefix}|" {} \;
popd

echo "*** Building gnutls ***"
pushd gnutls-*
LDFLAGS="-L%{xorg_buildroot}%{_libdir} -lgmp $LDFLAGS -static" PKG_CONFIG="pkg-config --static" ./configure \
  --prefix=%{_prefix} \
  --libdir=%{_libdir} \
  --enable-static \
  --disable-shared \
  --without-p11-kit \
  --disable-guile \
  --disable-srp-authentication \
  --disable-libdane \
  --disable-doc \
  --enable-local-libopts \
  --without-tpm \
  --disable-dependency-tracking \
  --disable-silent-rules \
  --disable-heartbeat-support
make %{?_smp_mflags} DESTDIR=%{xorg_buildroot} install
find %{xorg_buildroot}%{_prefix} -type f -name "*.la" -delete
find %{xorg_buildroot}%{_prefix} -type f -name "*.pc" -exec sed -i -e "s|libdir=%{_libdir}|libdir=%{xorg_buildroot}%{_libdir}|" {} \;
find %{xorg_buildroot}%{_prefix} -type f -name "*.pc" -exec sed -i -e "s|prefix=%{_prefix}|prefix=%{xorg_buildroot}%{_prefix}|" {} \;
popd

>>>>>>> 4c33f2ca86586bb8461526b93cba57a0a14c8baa
pushd xorg

echo "*** Building freetype ***"
pushd freetype-*
<<<<<<< HEAD
CFLAGS="$CFLAGS -fno-strict-aliasing" LDFLAGS="$LDFLAGS -static" ./configure --prefix=/usr --libdir=%{_libdir} --enable-static --disable-shared
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' builds/unix/libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' builds/unix/libtool
make DESTDIR=%{xorg_buildroot} install
find %{xorg_buildroot}%{_prefix} -type f -name "*.la" -exec sed -i -e "s|libdir='%{_libdir}'|libdir='%{xorg_buildroot}%{_libdir}'|" {} \;
find %{xorg_buildroot}%{_prefix} -type f -name "*.pc" -exec sed -i -e "s|libdir=%{_libdir}|libdir=%{xorg_buildroot}%{_libdir}|" {} \;
find %{xorg_buildroot}%{_prefix} -type f -name "*.pc" -exec sed -i -e "s|prefix=/usr|prefix=%{xorg_buildroot}%{_prefix}|" {} \;
=======
LDFLAGS="$LDFLAGS -static" PKG_CONFIG="pkg-config --static" CFLAGS="$CFLAGS -fno-strict-aliasing" ./configure --prefix=%{_prefix} --libdir=%{_libdir} --enable-static --disable-shared
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' builds/unix/libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' builds/unix/libtool
make DESTDIR=%{xorg_buildroot} install
# FIXME: fontconfig bails out if we delete the libtool archives
find %{xorg_buildroot}%{_prefix} -type f -name "*.la" -exec sed -i -e "s|libdir='%{_libdir}'|libdir='%{xorg_buildroot}%{_libdir}'|" {} \;
find %{xorg_buildroot}%{_prefix} -type f -name "*.pc" -exec sed -i -e "s|libdir=%{_libdir}|libdir=%{xorg_buildroot}%{_libdir}|" {} \;
find %{xorg_buildroot}%{_prefix} -type f -name "*.pc" -exec sed -i -e "s|prefix=%{_prefix}|prefix=%{xorg_buildroot}%{_prefix}|" {} \;
>>>>>>> 4c33f2ca86586bb8461526b93cba57a0a14c8baa
# fix multilib issues
%ifarch x86_64 s390x ia64 ppc64 alpha sparc64
%define wordsize 64
%else
%define wordsize 32
%endif

mv %{xorg_buildroot}%{_includedir}/freetype2/freetype/config/ftconfig.h \
   %{xorg_buildroot}%{_includedir}/freetype2/freetype/config/ftconfig-%{wordsize}.h
cat >%{xorg_buildroot}%{_includedir}/freetype2/freetype/config/ftconfig.h <<EOF
#ifndef __FTCONFIG_H__MULTILIB
#define __FTCONFIG_H__MULTILIB

#include <bits/wordsize.h>

#if __WORDSIZE == 32
# include "ftconfig-32.h"
#elif __WORDSIZE == 64
# include "ftconfig-64.h"
#else
# error "unexpected value for __WORDSIZE macro"
#endif

#endif 
EOF
popd

<<<<<<< HEAD
pushd util-macros-*
echo "Building macros"
./configure --prefix=/usr --libdir=%{_libdir} --disable-nls --enable-static --disable-shared
make DESTDIR=%{xorg_buildroot} install
find %{xorg_buildroot}%{_prefix} -type f -name "*.la" -exec sed -i -e "s|libdir='%{_libdir}'|libdir='%{xorg_buildroot}%{_libdir}'|" {} \;
find %{xorg_buildroot}%{_prefix} -type f -name "*.pc" -exec sed -i -e "s|libdir=%{_libdir}|libdir=%{xorg_buildroot}%{_libdir}|" {} \;
find %{xorg_buildroot}%{_prefix} -type f -name "*.pc" -exec sed -i -e "s|prefix=/usr|prefix=%{xorg_buildroot}%{_prefix}|" {} \;
=======
echo "*** Building fontconfig ***"
pushd fontconfig-*
autoreconf -fiv
LDFLAGS="$LDFLAGS -static" PKG_CONFIG="pkg-config --static" HASDOCBOOK=no ./configure --prefix=%{_prefix} --libdir=%{_libdir} --enable-static --disable-shared --with-confdir=%{_sysconfdir}/fonts --with-cache-dir=%{_localstatedir}/cache/fontconfig --with-default-fonts=%{_datadir}/fonts --with-add-fonts="%{_datadir}/X11/fonts/Type1,%{_datadir}/X11/fonts/OTF,%{_datadir}/X11/fonts/TTF,%{_datadir}/X11/fonts/misc,%{_datadir}/X11/fonts/100dpi,%{_datadir}/X11/fonts/75dpi,%{_prefix}/local/share/fonts,~/.fonts"
make %{?_smp_mflags}
make DESTDIR=%{xorg_buildroot} install
find %{xorg_buildroot}%{_prefix} -type f -name "*.la" -delete
find %{xorg_buildroot}%{_prefix} -type f -name "*.pc" -exec sed -i -e "s|libdir=%{_libdir}|libdir=%{xorg_buildroot}%{_libdir}|" {} \;
find %{xorg_buildroot}%{_prefix} -type f -name "*.pc" -exec sed -i -e "s|prefix=%{_prefix}|prefix=%{xorg_buildroot}%{_prefix}|" {} \;
popd

pushd util-macros-*
echo "Building macros"
LDFLAGS="$LDFLAGS -static" PKG_CONFIG="pkg-config --static" ./configure --prefix=%{_prefix} --libdir=%{_libdir} --enable-static --disable-shared
make DESTDIR=%{xorg_buildroot} install
find %{xorg_buildroot}%{_prefix} -type f -name "*.la" -delete
find %{xorg_buildroot}%{_prefix} -type f -name "*.pc" -exec sed -i -e "s|libdir=%{_libdir}|libdir=%{xorg_buildroot}%{_libdir}|" {} \;
find %{xorg_buildroot}%{_prefix} -type f -name "*.pc" -exec sed -i -e "s|prefix=%{_prefix}|prefix=%{xorg_buildroot}%{_prefix}|" {} \;
>>>>>>> 4c33f2ca86586bb8461526b93cba57a0a14c8baa
popd

modules="\
    bigreqsproto \
    compositeproto \
    damageproto \
    dri2proto \
    fixesproto \
    fontsproto \
    glproto \
    inputproto \
    kbproto \
    randrproto \
    recordproto \
    renderproto \
    resourceproto \
    scrnsaverproto \
    videoproto \
<<<<<<< HEAD
=======
    xcb-proto \
>>>>>>> 4c33f2ca86586bb8461526b93cba57a0a14c8baa
    xproto \
    xcmiscproto \
    xextproto \
    xf86bigfontproto \
    xf86dgaproto \
    xf86driproto \
    xf86vidmodeproto \
<<<<<<< HEAD
    xf86miscproto \
=======
>>>>>>> 4c33f2ca86586bb8461526b93cba57a0a14c8baa
    xineramaproto \
    makedepend \
    xtrans \
    libXau \
    libXdmcp \
<<<<<<< HEAD
    libpthread-stubs \
=======
    libxcb \
>>>>>>> 4c33f2ca86586bb8461526b93cba57a0a14c8baa
    libX11 \
    libXext \
    libfontenc \
    libICE \
    libSM \
    libXt \
    libXmu \
    libXpm \
    libXaw \
    libXfixes \
    libXcomposite \
    libXrender \
    libXdamage \
    libXcursor \
    libXfont \
    libXft \
    libXi \
    libXinerama \
    libxkbfile \
    libXrandr \
    libXres \
    libXScrnSaver \
    libXtst \
    libXv \
    libXxf86dga \
    libXxf86vm \
<<<<<<< HEAD
    libXxf86misc \
    libpciaccess \
    pixman \
    libdrm"
=======
    libpciaccess \
    pixman \
    libdrm \
    font-util"
>>>>>>> 4c33f2ca86586bb8461526b93cba57a0a14c8baa

for module in ${modules}; do
  extraoptions=""
  pushd ${module}-*
  echo ======================
  echo configuring ${module}
  echo ======================
<<<<<<< HEAD
%ifarch i386 i686
  if [ "${module}" = "libdrm" ]; then
    extraoptions="${extraoptions} --disable-intel"
  fi
%endif
  if [ "${module}" = "libXaw" ]; then
    extraoptions="${extraoptions} --disable-xaw8 --disable-xaw6"
  fi
  if [ "${module}" = "libX11" ]; then
    extraoptions="${extraoptions} --without-xcb --disable-specs"
=======
%ifarch i386 i686 x86_64
  if [ "${module}" = "libdrm" ]; then
    autoreconf -fiv
    extraoptions="${extraoptions} --enable-udev --disable-libkms --disable-manpages --disable-intel --disable-radeon --disable-nouveau --disable-vmwgfx"
  fi
%endif
  if [ "${module}" = "libXdmcp" ]; then
    autoreconf -fiv
  fi
  if [ "${module}" = "libXcursor" ]; then
    autoreconf -fiv
  fi
  if [ "${module}" = "libfontenc" ]; then
    autoconf
  fi
  if [ "${module}" = "libXi" ]; then
    autoreconf -fiv
  fi
  if [ "${module}" = "libXaw" ]; then
    extraoptions="${extraoptions} --disable-xaw8 --disable-xaw6"
  fi
  if [ "${module}" = "libxcb" ]; then
    sed -i 's/pthread-stubs //' configure.ac
    autoreconf -fiv
  fi
  if [ "${module}" = "libX11" ]; then
    autoreconf -fiv
    sed -i -e 's|^\(#pragma weak pthread_equal.*\)$||' src/UIThrStubs.c
    extraoptions="${extraoptions} --disable-specs"
>>>>>>> 4c33f2ca86586bb8461526b93cba57a0a14c8baa
  fi
  if [ "${module}" = "libSM" ]; then
    extraoptions="${extraoptions} --without-libuuid"
  fi
  if [ "${module}" = "pixman" ]; then
<<<<<<< HEAD
    extraoptions="${extraoptions} --disable-gtk"
=======
    extraoptions="${extraoptions} --disable-gtk --disable-openmp"
>>>>>>> 4c33f2ca86586bb8461526b93cba57a0a14c8baa
    aclocal -I %{xorg_buildroot}%{_datadir}/aclocal
    autoconf
    autoreconf -fiv
  fi
  if [ "${module}" = "libXfont" ]; then
    extraoptions="${extraoptions} --with-freetype-config=%{xorg_buildroot}%{_bindir}/freetype-config"
  fi
<<<<<<< HEAD
  if [ "${module}" = "libpthread-stubs" ]; then
    LDFLAGS="" ./configure --prefix=/usr --libdir=%{_libdir} ${extraoptions} --enable-static --disable-shared --with-pic
  elif [ "${module}" = "libX11" ]; then
    XDMCP_FLAGS="-L%{xorg_buildroot}%{_libdir} -Wl,-B,static -lXdmcp -lXau" ./configure --prefix=/usr --libdir=%{_libdir} ${extraoptions} --enable-static --disable-shared --with-pic
  elif [ "${module}" = "libXtst" ]; then
    XTST_FLAGS="-L%{xorg_buildroot}%{_libdir} -Wl,-B,static -lXext" ./configure --prefix=/usr --libdir=%{_libdir} ${extraoptions} --enable-static --disable-shared --with-pic
  else
    ./configure --prefix=/usr --libdir=%{_libdir} ${extraoptions} --enable-static --disable-shared --with-pic
=======
  if [ "${module}" = "libXScrnSaver" ]; then
    LDFLAGS="$LDFLAGS -static" PKG_CONFIG="pkg-config --static" CFLAGS="$CFLAGS -fno-strict-aliasing" ./configure --prefix=%{_prefix} --libdir=%{_libdir} ${extraoptions} --enable-static --disable-shared --with-pic
  elif [ "${module}" = "libxkbfile" ]; then
    LDFLAGS="$LDFLAGS -static" PKG_CONFIG="pkg-config --static" CFLAGS="$CFLAGS -fno-strict-aliasing" ./configure --prefix=%{_prefix} --libdir=%{_libdir} ${extraoptions} --enable-static --disable-shared --with-pic
  elif [ "${module}" = "pixman" ]; then
    LDFLAGS="$LDFLAGS -static" PKG_CONFIG="pkg-config --static" CFLAGS="$CFLAGS -fno-strict-aliasing" ./configure --prefix=%{_prefix} --libdir=%{_libdir} ${extraoptions} --enable-static --disable-shared --with-pic
  elif [ "${module}" = "libXt" ]; then
    LDFLAGS="$LDFLAGS -static" PKG_CONFIG="pkg-config --static" CFLAGS="$CFLAGS -fno-strict-aliasing" ./configure --prefix=%{_prefix} --libdir=%{_libdir} ${extraoptions} --enable-static --disable-shared --with-pic --with-xfile-search-path="%{_sysconfdir}/X11/%%L/%%T/%%N%%C%%S:%{_sysconfdir}/X11/%%l/%%T/\%%N%%C%%S:%{_sysconfdir}/X11/%%T/%%N%%C%%S:%{_sysconfdir}/X11/%%L/%%T/%%N%%S:%{_sysconfdir}/X\11/%%l/%%T/%%N%%S:%{_sysconfdir}/X11/%%T/%%N%%S:%{_datadir}/X11/%%L/%%T/%%N%%C%%S:%{_datadir}/X1\1/%%l/%%T/%%N%%C%%S:%{_datadir}/X11/%%T/%%N%%C%%S:%{_datadir}/X11/%%L/%%T/%%N%%S:%{_datadir}/X11/%%\l/%%T/%%N%%S:%{_datadir}/X11/%%T/%%N%%S"
  elif [ "${module}" = "libX11" ]; then
    LDFLAGS="$LDFLAGS -static" PKG_CONFIG="pkg-config --static" ./configure --prefix=%{_prefix} --libdir=%{_libdir} ${extraoptions} --enable-static --disable-shared --with-pic
  elif [ "${module}" = "libXtst" ]; then
    LDFLAGS="$LDFLAGS -static" PKG_CONFIG="pkg-config --static" ./configure --prefix=%{_prefix} --libdir=%{_libdir} ${extraoptions} --enable-static --disable-shared --with-pic
  elif [ "${module}" = "libXpm" ]; then
    LDFLAGS="$LDFLAGS -static" PKG_CONFIG="pkg-config --static" ./configure --prefix=%{_prefix} --libdir=%{_libdir} ${extraoptions} --enable-static --disable-shared --with-pic
  else
    LDFLAGS="$LDFLAGS -static" PKG_CONFIG="pkg-config --static" ./configure --prefix=%{_prefix} --libdir=%{_libdir} ${extraoptions} --enable-static --disable-shared --with-pic
>>>>>>> 4c33f2ca86586bb8461526b93cba57a0a14c8baa
  fi
  echo ======================
  echo building ${module}
  echo ======================
<<<<<<< HEAD
  make DESTDIR=%{xorg_buildroot} install
  find %{xorg_buildroot}%{_prefix} -type f -name "*.la" -exec sed -i -e "s|libdir='%{_libdir}'|libdir='%{xorg_buildroot}%{_libdir}'|" {} \;
  find %{xorg_buildroot}%{_prefix} -type f -name "*.pc" -exec sed -i -e "s|libdir=%{_libdir}|libdir=%{xorg_buildroot}%{_libdir}|" {} \;
  find %{xorg_buildroot}%{_prefix} -type f -name "*.pc" -exec sed -i -e "s|prefix=/usr|prefix=%{xorg_buildroot}%{_prefix}|" {} \;
=======
  make DESTDIR=%{xorg_buildroot}
  if [ "${module}" = "libX11" ]; then
    make DESTDIR=%{xorg_buildroot} INSTALL="install -p" install
  else
    make DESTDIR=%{xorg_buildroot} install
  fi
  find %{xorg_buildroot}%{_prefix} -type f -name "*.la" -delete
  find %{xorg_buildroot}%{_prefix} -type f -name "*.pc" -exec sed -i -e "s|libdir=%{_libdir}|libdir=%{xorg_buildroot}%{_libdir}|" {} \;
  find %{xorg_buildroot}%{_prefix} -type f -name "*.pc" -exec sed -i -e "s|prefix=%{_prefix}|prefix=%{xorg_buildroot}%{_prefix}|" {} \;
  if [ "${module}" = "libxcb" ]; then
    sed 's,@libdir@,%{xorg_buildroot}%{_libdir},;s,@prefix@,%{xorg_buildroot}%{_prefix},;s,@exec_prefix@,%{xorg_buildroot}%{_exec_prefix},' %{SOURCE140} > %{xorg_buildroot}%{_libdir}/pkgconfig/pthread-stubs.pc
    sed -i -e 's/^\(Libs.private:.*\)$/\1 -L${libdir} -lXdmcp -lXau/' %{xorg_buildroot}%{_libdir}/pkgconfig/xcb.pc 
  elif [ "${module}" = "libX11" ]; then
    sed -i -e 's/^\(Libs:.*\)$/\1 -ldl/' %{xorg_buildroot}%{_libdir}/pkgconfig/x11.pc 
    sed -i -e 's/^\(Libs.private:.*\)$/\1 -L${libdir} -lxcb/' %{xorg_buildroot}%{_libdir}/pkgconfig/x11.pc 
  elif [ "${module}" = "libSM" ]; then
    echo 'Libs.private: -L${libdir} -lICE' >> %{xorg_buildroot}%{_libdir}/pkgconfig/sm.pc
  fi

>>>>>>> 4c33f2ca86586bb8461526b93cba57a0a14c8baa
  popd
done

# build mesa
echo "*** Building Mesa ***"
pushd Mesa-*
<<<<<<< HEAD
%ifarch %{ix86}
# i do not have words for how much the assembly dispatch code infuriates me
%define _mesa_flags --enable-pic --disable-asm
%else
%define _mesa_flags --enable-pic
%endif

# Need to set cfghost?
./configure \
  --prefix=/usr \
  --libdir=%{_libdir} \
  --enable-motif \
  --with-driver=dri \
  --with-dri-drivers=swrast \
  --with-dri-driverdir=%{_libdir}/dri \
  --with-gallium-drivers="" \
  --without-demos \
  --disable-driglx-direct \
  --disable-egl \
  --disable-glut \
  --disable-gallium \
  --disable-gl-osmesa \
  --disable-gallium-intel \
  --disable-gallium-radeon \
  --disable-gallium-nouveau \
  %{_mesa_flags}

# Mesa build fails to install libGLU* if 'make install' is run before 'make'
make DESTDIR=%{xorg_buildroot}
make DESTDIR=%{xorg_buildroot} install
find %{xorg_buildroot}%{_prefix} -type f -name "*.la" -exec sed -i -e "s|libdir='%{_libdir}'|libdir='%{xorg_buildroot}%{_libdir}'|" {} \;
find %{xorg_buildroot}%{_prefix} -type f -name "*.pc" -exec sed -i -e "s|libdir=%{_libdir}|libdir=%{xorg_buildroot}%{_libdir}|" {} \;
find %{xorg_buildroot}%{_prefix} -type f -name "*.pc" -exec sed -i -e "s|prefix=/usr|prefix=%{xorg_buildroot}%{_prefix}|" {} \;
=======
export PYTHON2=python26
%ifarch %{ix86}
sed -i -e 's/-std=c99/-std=gnu99/g' configure.ac
%endif
autoreconf -fiv
%ifarch %{ix86}
# i do not have words for how much the assembly dispatch code infuriates me
%define common_flags --disable-selinux --enable-pic --disable-asm
%else
%define common_flags --disable-selinux --enable-pic
%endif

# link libGL statically against any xorg libraries built above
LDFLAGS="$LDFLAGS -Wl,-Bstatic -lxcb -lX11 -lXdmcp -lXau -lXext -lXxf86vm -ldrm -Wl,-Bdynamic -Wl,-rpath,%{_libdir}/tigervnc:%{_libdir}" \
PKG_CONFIG="pkg-config --static" ./configure %{common_flags} \
    --prefix=%{_prefix} \
    --libdir=%{_libdir}/tigervnc \
    --disable-osmesa \
    --disable-shared-glapi \
    --disable-egl \
    --disable-gbm \
    --enable-glx \
    --disable-glx-tls \
    --disable-opencl \
    --disable-xvmc \
    --with-dri-driverdir=%{_libdir}/tigervnc/dri \
    --disable-gallium-egl \
    --with-gallium-drivers="" \
    --with-dri-drivers=swrast

make DESTDIR=%{xorg_buildroot}
make install DESTDIR=%{xorg_buildroot}
find %{xorg_buildroot}%{_prefix} -type f -name "*.la" -delete
find %{xorg_buildroot}%{_prefix} -type f -name "*.pc" -exec sed -i -e "s|libdir=%{_libdir}|libdir=%{xorg_buildroot}%{_libdir}|" {} \;
find %{xorg_buildroot}%{_prefix} -type f -name "*.pc" -exec sed -i -e "s|prefix=%{_prefix}|prefix=%{xorg_buildroot}%{_prefix}|" {} \;
>>>>>>> 4c33f2ca86586bb8461526b93cba57a0a14c8baa
popd

popd

<<<<<<< HEAD
echo "*** Building fontconfig ***"
pushd fontconfig-*
HASDOCBOOK=no ./configure --prefix=%{_prefix} --libdir=%{_libdir} --with-add-fonts=/usr/share/X11/fonts/Type1,/usr/share/X11/fonts/OTF --enable-static --disable-shared
make %{?_smp_mflags}
make DESTDIR=%{xorg_buildroot} install
find %{xorg_buildroot}%{_prefix} -type f -name "*.la" -exec sed -i -e "s|libdir='%{_libdir}'|libdir='%{xorg_buildroot}%{_libdir}'|" {} \;
find %{xorg_buildroot}%{_prefix} -type f -name "*.pc" -exec sed -i -e "s|libdir=%{_libdir}|libdir=%{xorg_buildroot}%{_libdir}|" {} \;
find %{xorg_buildroot}%{_prefix} -type f -name "*.pc" -exec sed -i -e "s|prefix=/usr|prefix=%{xorg_buildroot}%{_prefix}|" {} \;
=======
echo "*** Building libpng ***"
pushd libpng-*
CFLAGS="${CFLAGS}" CXXFLAGS="${CXXFLAGS}" LDFLAGS="${LDFLAGS}" ./configure \
  --prefix=%{_prefix} \
  --libdir=%{_libdir} \
  --disable-shared \
  --enable-static
make %{?_smp_mflags}
make DESTDIR=%{xorg_buildroot} install
>>>>>>> 4c33f2ca86586bb8461526b93cba57a0a14c8baa
popd

echo "*** Building fltk ***"
pushd fltk-*
export CMAKE_PREFIX_PATH="%{xorg_buildroot}%{_prefix}:%{_prefix}"
<<<<<<< HEAD
export CMAKE_EXE_LINKER_FLAGS="-static-libgcc -L%{xorg_buildroot}%{_libdir}"
%{cmake28} -G"Unix Makefiles" \
  -DCMAKE_INSTALL_PREFIX=%{xorg_buildroot}%{_prefix} \
  -DX11_INC_SEARCH_PATH=%{xorg_buildroot}%{_includedir} \
  -DX11_LIB_SEARCH_PATH=%{xorg_buildroot}%{_libdir} \
  -DCMAKE_BUILD_TYPE=Release \
  -DOPTION_USE_THREADS=off \
  -DOPTION_BUILD_EXAMPLES=off \
  -DOPTION_USE_SYSTEM_LIBPNG=on
make %{?_smp_mflags}
=======
export CMAKE_EXE_LINKER_FLAGS=$LDFLAGS
export PKG_CONFIG="pkg-config --static" 
CFLAGS="${CFLAGS}" CXXFLAGS="${CXXFLAGS}" LDFLAGS="${LDFLAGS}" ./configure \
  --prefix=%{_prefix} \
  --libdir=%{_libdir} \
  --enable-x11 \
  --enable-gl \
  --disable-shared \
  --enable-localjpeg \
  --enable-localzlib \
  --disable-localpng \
  --enable-xinerama \
  --enable-xft \
  --enable-xdbe \
  --enable-xfixes \
  --enable-xcursor \
  --with-x 
make %{?_smp_mflags}
make DESTDIR=%{xorg_buildroot} install
>>>>>>> 4c33f2ca86586bb8461526b93cba57a0a14c8baa
popd

echo "*** Building VNC ***"
export CFLAGS="$CFLAGS -fPIC"
export CXXFLAGS=`echo $CXXFLAGS | sed -e 's/ -c //g'`
%{cmake28} -G"Unix Makefiles" \
<<<<<<< HEAD
  -DX11_INC_SEARCH_PATH=%{xorg_buildroot}%{_includedir} \
  -DX11_LIB_SEARCH_PATH=%{xorg_buildroot}%{_libdir} \
  -DFLTK_LIBRARY_DIR=%{tigervnc_src_dir}/fltk-1.3.2/lib \
  -DFLTK_LIBRARIES="%{tigervnc_src_dir}/fltk-1.3.2/lib/libfltk.a;%{tigervnc_src_dir}/fltk-1.3.2/lib/libfltk_images.a;-lpng" \
  -DFLTK_FLUID_EXECUTABLE=%{tigervnc_src_dir}/fltk-1.3.2/bin/fluid \
  -DFLTK_INCLUDE_DIR=%{tigervnc_src_dir}/fltk-1.3.2 \
  -DBUILD_STATIC=1 \
  -DCMAKE_BUILD_TYPE=Release \
  -DUSE_INCLUDED_ZLIB=0 \
=======
  -DFLTK_FLUID_EXECUTABLE=%{xorg_buildroot}%{_bindir}/fluid \
  -DFLTK_LIBRARY_DIR=%{xorg_buildroot}%{_libdir} \
  -DFLTK_INCLUDE_DIR=%{xorg_buildroot}%{_includedir} \
  -DBUILD_STATIC=1 \
  -DCMAKE_BUILD_TYPE=Release \
  -DUSE_INCLUDED_ZLIB=0 \
  -DZLIB_INCLUDE_DIR=%{_includedir} \
  -DZLIB_LIBRARY=%{_libdir}/libz.a \
>>>>>>> 4c33f2ca86586bb8461526b93cba57a0a14c8baa
  -DCMAKE_INSTALL_PREFIX=%{_prefix}

make %{?_smp_mflags}

pushd unix/xserver
<<<<<<< HEAD
export LD=$CXX
export PIXMANINCDIR=%{xorg_buildroot}%{_includedir}/pixman-1
autoreconf -fiv 
./configure --prefix=/usr --libdir=%{_libdir} --mandir=%{_datadir}/man \
	--disable-xorg --disable-xnest --disable-xvfb --disable-dmx \
	--disable-xwin --disable-xephyr --disable-kdrive --with-pic \
	--disable-xinerama \
	--with-int10=x86emu \
	--enable-xdmcp \
	--enable-composite \
	--disable-xgl \
	--disable-xglx \
	--enable-freetype \
	--with-fontdir=%{_datadir}/X11/fonts \
	--with-xkb-output=%{_localstatedir}/lib/xkb \
	--enable-install-libxf86config \
	--enable-glx --disable-dri --enable-dri2 \
	--disable-config-dbus \
	--disable-config-hal \
	--disable-config-udev \
	--with-dri-driver-path=%{_libdir}/dri \
	--without-dtrace \
	--disable-unit-tests \
	--disable-devel-docs \
	--with-sha1=libgcrypt SHA1_LIB=-lcrypto \
	--disable-shared \
	--enable-static \
	--disable-record \
	--enable-aiglx \
	--disable-xvmc \
	--enable-dga \
	--disable-screensaver \
	--enable-xdm-auth-1 \
	--enable-xf86vidmode \
	--enable-xcsecurity \
	--enable-appgroup \
	--enable-xevie \
	--enable-evi \
	--enable-multibuffer \
	--enable-xf86bigfont \
	--disable-dpms \
	--disable-ipv6 \
	--with-mesa-source=%{tigervnc_src_dir}/xorg/Mesa-%{mesa_version} \
	--with-freetype-config=%{xorg_buildroot}%{_bindir}/freetype-config \
	--disable-maintainer-mode

sed -i -e 's/^ECHO/echo/' ./libtool
=======
export PIXMANINCDIR=%{xorg_buildroot}%{_includedir}/pixman-1
sed -i -e 's/^\(\s*WAYLAND_SCANNER_RULES.*\)/dnl\1/' configure.ac
autoreconf -fiv 
chmod +x ./configure
# create a relocatable Xvnc so that we can bundle the custom libGL & swrast w/o overwriting existing libs
GL_LIBS='-Wl,-Bdynamic -lGL' LDFLAGS="$LDFLAGS -L%{xorg_buildroot}%{_libdir}/tigervnc -Wl,-rpath,%{_libdir}/tigervnc:%{_libdir}" \
%configure \
  --prefix=%{_prefix} --libdir=%{_libdir} --mandir=%{_datadir}/man \
  --sysconfdir=%{_sysconfdir} --localstatedir=%{_localstatedir} \
  --with-vendor-name="The TigerVNC Project" --with-vendor-name-short="TigerVNC" \
  --with-vendor-web="http://www.tigervnc.org" \
  --disable-xorg --disable-xnest --disable-xvfb --disable-dmx \
  --disable-xwin --disable-xephyr --disable-kdrive --disable-wayland \
  --with-pic --enable-static --disable-shared --enable-xinerama \
  --with-default-xkb-rules=base \
  --with-default-font-path="catalogue:%{_sysconfdir}/X11/fontpath.d,%{_datadir}/X11/fonts/misc,%{_datadir}/X11/fonts/OTF,%{_datadir}/X11/fonts/TTF,%{_datadir}/X11/fonts/Type1,%{_datadir}/X11/fonts/100dpi,%{_datadir}/X11/fonts/75dpi,built-ins" \
  --with-serverconfig-path=%{_libdir}/xorg \
  --with-fontrootdir=%{_datadir}/X11/fonts \
  --with-xkb-output=%{_localstatedir}/lib/xkb \
  --enable-install-libxf86config \
  --enable-glx --disable-glx-tls --disable-dri --enable-dri2 --disable-dri3 \
  --disable-present \
  --disable-config-dbus \
  --disable-config-hal \
  --disable-config-udev \
  --without-dtrace \
  --disable-unit-tests \
  --disable-docs \
  --disable-devel-docs \
  --disable-selective-werror \
  --with-sha1=libsha1
>>>>>>> 4c33f2ca86586bb8461526b93cba57a0a14c8baa

make TIGERVNC_SRCDIR=%{tigervnc_src_dir} %{?_smp_mflags}
popd

# Build icons
pushd media
make
popd

# Build Java applet
pushd java
%{cmake28} \
%if !%{_self_signed}
<<<<<<< HEAD
	-DJAVA_KEYSTORE=%{_keystore} \
	-DJAVA_KEYSTORE_TYPE=%{_keystore_type} \
	-DJAVA_KEY_ALIAS=%{_key_alias} \
	-DJAVA_STOREPASS=":env STOREPASS" \
	-DJAVA_KEYPASS=":env KEYPASS" \
	-DJAVA_TSA_URL=https://timestamp.geotrust.com/tsa .
=======
  -DJAVA_KEYSTORE=%{_keystore} \
  -DJAVA_KEYSTORE_TYPE=%{_keystore_type} \
  -DJAVA_KEY_ALIAS=%{_key_alias} \
  -DJAVA_STOREPASS=":env STOREPASS" \
  -DJAVA_KEYPASS=":env KEYPASS" \
  -DJAVA_TSA_URL=https://timestamp.geotrust.com/tsa .
>>>>>>> 4c33f2ca86586bb8461526b93cba57a0a14c8baa
%endif

JAVA_TOOL_OPTIONS="-Dfile.encoding=UTF8" make
popd

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

pushd unix/xserver/hw/vnc
make install DESTDIR=$RPM_BUILD_ROOT
popd

<<<<<<< HEAD
=======
pushd xorg/Mesa-*
make install DESTDIR=$RPM_BUILD_ROOT
popd

>>>>>>> 4c33f2ca86586bb8461526b93cba57a0a14c8baa
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/init.d
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig
install -m644 %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/init.d/vncserver
install -m644 %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/vncservers

# Install desktop stuff
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/{16x16,24x24,48x48}/apps

pushd media/icons
for s in 16 24 48; do
install -m644 tigervnc_$s.png $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/${s}x$s/apps/tigervnc.png
done
popd

mkdir $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install \
	--dir $RPM_BUILD_ROOT%{_datadir}/applications \
	--vendor="" \
	%{SOURCE6}

# Install Java applet
pushd java
mkdir -p $RPM_BUILD_ROOT%{_datadir}/vnc/classes
install -m755 VncViewer.jar $RPM_BUILD_ROOT%{_datadir}/vnc/classes
install -m644 com/tigervnc/vncviewer/index.vnc $RPM_BUILD_ROOT%{_datadir}/vnc/classes
popd

%find_lang %{name} %{name}.lang

# remove unwanted files
<<<<<<< HEAD
rm -f $RPM_BUILD_ROOT%{_libdir}/xorg/modules/extensions/libvnc.la
rm -f $RPM_BUILD_ROOT%{_libdir}/xorg/modules/extensions/libvnc.a
rm -f $RPM_BUILD_ROOT%{_libdir}/dri/libdricore.so

# move files to correct location
mkdir -p $RPM_BUILD_ROOT%{_libdir}/dri
cp %{xorg_buildroot}%{_libdir}/dri/* $RPM_BUILD_ROOT%{_libdir}/dri/
=======
rm -rf $RPM_BUILD_ROOT%{_libdir}/tigervnc/pkgconfig
rm -rf $RPM_BUILD_ROOT%{_libdir}/pkgconfig
rm -rf $RPM_BUILD_ROOT%{_libdir}/xorg
rm -rf $RPM_BUILD_ROOT%{_includedir}
rm -f $RPM_BUILD_ROOT%{_libdir}/tigervnc/*.la
rm -f $RPM_BUILD_ROOT%{_libdir}/tigervnc/dri/*.la
>>>>>>> 4c33f2ca86586bb8461526b93cba57a0a14c8baa

%clean
rm -rf $RPM_BUILD_ROOT

%post
touch -c %{_datadir}/icons/hicolor
if [ -x %{_bindir}/gtk-update-icon-cache ]; then
	%{_bindir}/gtk-update-icon-cache -q %{_datadir}/icons/hicolor || :
fi

%postun
touch -c %{_datadir}/icons/hicolor
if [ -x %{_bindir}/gtk-update-icon-cache ]; then
	%{_bindir}/gtk-update-icon-cache -q %{_datadir}/icons/hicolor || :
fi

%post server
/sbin/chkconfig --add vncserver

%preun server
if [ $1 -eq 0 ]; then
	/sbin/service vncserver stop &>/dev/null || :
	/sbin/chkconfig --del vncserver
fi

%postun server
/sbin/service vncserver condrestart &>/dev/null || :

%files -f %{name}.lang
%defattr(-,root,root,-)
%doc README.txt
%{_bindir}/vncviewer
%{_datadir}/applications/*
%{_mandir}/man1/vncviewer.1*

%files server
%defattr(-,root,root,-)
%config(noreplace) %{_sysconfdir}/sysconfig/vncservers
%config(noreplace) %{_sysconfdir}/init.d/vncserver
%{_bindir}/x0vncserver
%{_bindir}/vncserver
%{_mandir}/man1/vncserver.1*
%{_mandir}/man1/x0vncserver.1*

%files server-minimal
%defattr(-,root,root,-)
%{_bindir}/vncconfig
%{_bindir}/vncpasswd
%{_bindir}/Xvnc
%{_mandir}/man1/Xvnc.1*
%{_mandir}/man1/vncpasswd.1*
%{_mandir}/man1/vncconfig.1*
<<<<<<< HEAD
%{_libdir}/dri/swrast_dri.so
=======
%{_libdir}/*
>>>>>>> 4c33f2ca86586bb8461526b93cba57a0a14c8baa

%files server-applet
%defattr(-,root,root,-)
%doc java/com/tigervnc/vncviewer/README
%{_datadir}/vnc/classes/*

%files license
%defattr(-,root,root,-)
%doc LICENCE.TXT

%files icons
%defattr(-,root,root,-)
%{_datadir}/icons/hicolor/*/apps/*

%changelog
<<<<<<< HEAD
=======
* Sat Mar 14 2015 Brian P. Hinz <bphinz@users.sourceforge.net> 1.4.80-6
- Build static libraries to meet new minimum requirements

* Sat Mar 07 2015 Brian P. Hinz <bphinz@users.sourceforge.net> 1.4.80-5
- Don't disable xinerama extension

* Thu Feb 19 2015 Brian P. Hinz <bphinz@users.sourceforge.net> 1.4.80-4
- Bumped fltk to 1.3.3, no longer requires patching

* Mon Jan 19 2015 Brian P. Hinz <bphinz@users.sourceforge.net> 1.4.0-3
- Added default font paths to Xvnc and fontconfig
- Added vendor strings to Xvnc
- Specified xfile-search-path when configuring libXt the same way el6 does

* Wed Dec 24 2014 Brian P. Hinz <bphinz@users.sourceforge.net> 1.4.80-1.20141119git59c5a55c
- Rebuilt against Xorg 7.7 with CVE-2104-12-09 patches from debian.
- Bumped versions of Mesa, Freetype, fontconfig, etc.
- Link against our own version of libGL to improve portability.
- Added static libsha1 to avoid linking against libssl.so.

>>>>>>> 4c33f2ca86586bb8461526b93cba57a0a14c8baa
* Wed Nov 19 2014 Brian P. Hinz <bphinz@users.sourceforge.net> 1.3.80-18.20141119git59c5a55c
- Removed server module sub-package

* Thu Nov 28 2013 Brian P. Hinz <bphinz@users.sourceforge.net> 1.3.80-17.20131128svn5139
- Bumped version to 1.3.80
- Cleaned up linter warnings

* Thu Jul 05 2013 Brian P. Hinz <bphinz@users.sourceforge.net> 1.3.0
- Upstream 1.3.0 release
- Conditional-ized %snap for release

* Fri Jun 14 2013 Brian P. Hinz <bphinz@users.sourceforge.net> 1.2.90-14.20130531svn5120
- Update libjpeg-turbo to 1.3.0

* Fri May 24 2013 Brian P. Hinz <bphinz@users.sourceforge.net> 1.2.90-14.20130524svn5114
- Improve spec file portability

* Fri May 17 2013 Brian P. Hinz <bphinz@users.sourceforge.net> 1.2.90-13.20130425svn5087
- Improve portability with more static linking

* Thu Apr 04 2013 Brian P. Hinz <bphinz@users.sourceforge.net> 1.2.80-12.20130330svn5066
- Added conditional -march arg to libdrm-intel to allow building on i386
- Fixed version to reflect upstream pre-release versioning

* Sat Mar 30 2013 Brian P. Hinz <bphinz@users.sourceforge.net> 1.2.0-11.20130330svn5066
- Updated to TigerVNC svn 5066
- Updated fltk to 1.3.2 and updated fltk patches per BUILDING.txt
- Fixed vncserver init script & config file which had been overwritten by 
  systemd versions.

* Wed Nov 28 2012 Brian P. Hinz <bphinz@users.sourceforge.net> 1.2.0-7.20120915svn4999
- Changed BuildRequires to cmake28 
- Set PIXMANINCDIR when building Xvnc

* Tue Sep 18 2012 Brian P. Hinz <bphinz@users.sourceforge.net> 1.2.0-6.20120915svn4999
- Applied icon support patch

* Sat Sep 15 2012 Brian P. Hinz <bphinz@users.sourceforge.net> 1.2.0-5.20120915svn4999
- Update to TigerVNC svn r4999 snapshot
- Build a static libjpeg-turbo to remove the external dependency
- Applied Cendio's Fltk patches, except for the icon patch which I cannot get to build
  without creating undefined reference errors during linking

* Thu Jul 19 2012 Brian P. Hinz <bphinz@users.sourceforge.net> 1.2.0-4.20120719svn4941
- Update to TigerVNC svn r4941 snapshot
- Removed border-hook.patch since it's been committed

* Wed Jul 18 2012 Brian P. Hinz <bphinz@users.sourceforge.net> 1.2.0-3.20120715svn4937
- Update to TigerVNC svn r4937 snapshot
- Applied border-hook.patch from devel list to fix bug #3415308
- Use build order recommended by cgit.freedesktop.org/xorg/util/modular/tree/build.sh
- Removed tigervnc11-rh692048.patch as it seems to break support for VeNCrypt

* Sun Jul 15 2012 Brian P. Hinz <bphinz@users.sourceforge.net> 1.2.0-1.20120715svn4935
- Adapted spec file for building static linked binary on RHEL5 from F16
  spec file and DRC's build-xorg script included in src tarball.
- Update to TigerVNC svn r4935 snapshot
- Need to use inkscape on RHEL5 because convert is broken

* Tue Nov 22 2011 Adam Tkac <atkac redhat com> - 1.1.0-3
- don't build X.Org devel docs (#755782)
- applet: BR generic java-devel instead of java-gcj-devel (#755783)
- use runuser to start Xvnc in systemd service file (#754259)
- don't attepmt to restart Xvnc session during update/erase (#753216)

* Fri Nov 11 2011 Adam Tkac <atkac redhat com> - 1.1.0-2
- libvnc.so: don't use unexported GetMaster function (#744881)
- remove nasm buildreq

* Mon Sep 12 2011 Adam Tkac <atkac redhat com> - 1.1.0-1
- update to 1.1.0
- update the xorg11 patch
- patches merged
  - tigervnc11-glx.patch
  - tigervnc11-CVE-2011-1775.patch
  - 0001-Use-memmove-instead-of-memcpy-in-fbblt.c-when-memory.patch

* Thu Jul 28 2011 Adam Tkac <atkac redhat com> - 1.0.90-6
- add systemd service file and remove legacy SysV initscript (#717227)

* Tue May 12 2011 Adam Tkac <atkac redhat com> - 1.0.90-5
- make Xvnc buildable against X.Org 1.11

* Tue May 10 2011 Adam Tkac <atkac redhat com> - 1.0.90-4
- viewer can send password without proper validation of X.509 certs
  (CVE-2011-1775)

* Wed Apr 13 2011 Adam Tkac <atkac redhat com> - 1.0.90-3
- fix wrong usage of memcpy which caused screen artifacts (#652590)
- don't point to inaccessible link in sysconfig/vncservers (#644975)

* Fri Apr 08 2011 Adam Tkac <atkac redhat com> - 1.0.90-2
- improve compatibility with vinagre client (#692048)

* Tue Mar 22 2011 Adam Tkac <atkac redhat com> - 1.0.90-1
- update to 1.0.90

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.90-0.32.20110117svn4237
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jan 17 2011 Adam Tkac <atkac redhat com> 1.0.90-0.31.20110117svn4237
- fix libvnc.so module loading

* Mon Jan 17 2011 Adam Tkac <atkac redhat com> 1.0.90-0.30.20110117svn4237
- update to r4237
- patches merged
  - tigervnc11-optionsdialog.patch
  - tigervnc11-rh607866.patch

* Fri Jan 14 2011 Adam Tkac <atkac redhat com> 1.0.90-0.29.20101208svn4225
- improve patch for keyboard issues

* Fri Jan 14 2011 Adam Tkac <atkac redhat com> 1.0.90-0.28.20101208svn4225
- attempt to fix various keyboard-related issues (key repeating etc)

* Fri Jan 07 2011 Adam Tkac <atkac redhat com> 1.0.90-0.27.20101208svn4225
- render "Ok" and "Cancel" buttons in the options dialog correctly

* Wed Dec 15 2010 Jan Görig <jgorig redhat com> 1.0.90-0.26.20101208svn4225
- added vncserver lock file (#662784)

* Fri Dec 10 2010 Adam Tkac <atkac redhat com> 1.0.90-0.25.20101208svn4225
- update to r4225
- patches merged
  - tigervnc11-rh611677.patch
  - tigervnc11-rh633931.patch
  - tigervnc11-xorg1.10.patch
- enable VeNCrypt and PAM support

* Mon Dec 06 2010 Adam Tkac <atkac redhat com> 1.0.90-0.24.20100813svn4123
- rebuild against xserver 1.10.X
- 0001-Return-Success-from-generate_modkeymap-when-max_keys.patch merged

* Wed Sep 29 2010 jkeating - 1.0.90-0.23.20100813svn4123
- Rebuilt for gcc bug 634757

* Tue Sep 21 2010 Adam Tkac <atkac redhat com> 1.0.90-0.22.20100420svn4030
- drop xorg-x11-fonts-misc dependency (#636170)

* Tue Sep 21 2010 Adam Tkac <atkac redhat com> 1.0.90-0.21.20100420svn4030
- improve patch for #633645 (fix tcsh incompatibilities)

* Thu Sep 16 2010 Adam Tkac <atkac redhat com> 1.0.90-0.20.20100813svn4123
- press fake modifiers correctly (#633931)
- supress unneeded debug information emitted from initscript (#633645)

* Wed Aug 25 2010 Adam Tkac <atkac redhat com> 1.0.90-0.19.20100813svn4123
- separate Xvnc, vncpasswd and vncconfig to -server-minimal subpkg (#626946)
- move license to separate subpkg and Requires it from main subpkgs
- Xvnc: handle situations when no modifiers exist well (#611677)

* Fri Aug 13 2010 Adam Tkac <atkac redhat com> 1.0.90-0.18.20100813svn4123
- update to r4123 (#617973)
- add perl requires to -server subpkg (#619791)

* Thu Jul 22 2010 Adam Tkac <atkac redhat com> 1.0.90-0.17.20100721svn4113
- update to r4113
- patches merged
  - tigervnc11-rh586406.patch
  - tigervnc11-libvnc.patch
  - tigervnc11-rh597172.patch
  - tigervnc11-rh600070.patch
  - tigervnc11-options.patch
- don't own %%{_datadir}/icons directory (#614301)
- minor improvements in the .desktop file (#616340)
- bundled libjpeg configure requires nasm; is executed even if system-wide
  libjpeg is used

* Fri Jul 02 2010 Adam Tkac <atkac redhat com> 1.0.90-0.16.20100420svn4030
- build against system-wide libjpeg-turbo (#494458)
- build no longer requires nasm

* Mon Jun 28 2010 Adam Tkac <atkac redhat com> 1.0.90-0.15.20100420svn4030
- vncserver: accept <+optname> option when specified as the first one

* Thu Jun 24 2010 Adam Tkac <atkac redhat com> 1.0.90-0.14.20100420svn4030
- fix memory leak in Xvnc input code (#597172)
- don't crash when receive negative encoding (#600070)
- explicitly disable udev configuration support
- add gettext-autopoint to BR

* Mon Jun 14 2010 Adam Tkac <atkac redhat com> 1.0.90-0.13.20100420svn4030
- update URL about SSH tunneling in the sysconfig file (#601996)

* Fri Jun 11 2010 Adam Tkac <atkac redhat com> 1.0.90-0.12.20100420svn4030
- use newer gettext
- autopoint now uses git instead of cvs, adjust BuildRequires appropriately

* Thu May 13 2010 Adam Tkac <atkac redhat com> 1.0.90-0.11.20100420svn4030
- link libvnc.so "now" to catch "undefined symbol" errors during Xorg startup
- use always XkbConvertCase instead of XConvertCase (#580159, #586406)
- don't link libvnc.so against libXi.la, libdix.la and libxkb.la; use symbols
  from Xorg instead

* Thu May 13 2010 Adam Tkac <atkac redhat com> 1.0.90-0.10.20100420svn4030
- update to r4030 snapshot
- patches merged to upstream
  - tigervnc11-rh522369.patch
  - tigervnc11-rh551262.patch
  - tigervnc11-r4002.patch
  - tigervnc11-r4014.patch

* Thu Apr 08 2010 Adam Tkac <atkac redhat com> 1.0.90-0.9.20100219svn3993
- add server-applet subpackage which contains Java vncviewer applet
- fix Java applet; it didn't work when run from web browser
- add xorg-x11-xkb-utils to server Requires

* Fri Mar 12 2010 Adam Tkac <atkac redhat com> 1.0.90-0.8.20100219svn3993
- add French translation to vncviewer.desktop (thanks to Alain Portal)

* Thu Mar 04 2010 Adam Tkac <atkac redhat com> 1.0.90-0.7.20100219svn3993
- don't crash during pixel format change (#522369, #551262)

* Mon Mar 01 2010 Adam Tkac <atkac redhat com> 1.0.90-0.6.20100219svn3993
- add mesa-dri-drivers and xkeyboard-config to -server Requires
- update to r3993 1.0.90 snapshot
  - tigervnc11-noexecstack.patch merged
  - tigervnc11-xorg18.patch merged
  - xserver18.patch is no longer needed

* Wed Jan 27 2010 Jan Gorig <jgorig redhat com> 1.0.90-0.5.20091221svn3929
- initscript LSB compliance fixes (#523974)

* Fri Jan 22 2010 Adam Tkac <atkac redhat com> 1.0.90-0.4.20091221svn3929
- mark stack as non-executable in jpeg ASM code
- add xorg-x11-xauth to Requires
- add support for X.Org 1.8
- drop shave sources, they are no longer needed

* Thu Jan 21 2010 Adam Tkac <atkac redhat com> 1.0.90-0.3.20091221svn3929
- drop tigervnc-xorg25909.patch, it has been merged to X.Org upstream

* Thu Jan 07 2010 Adam Tkac <atkac redhat com> 1.0.90-0.2.20091221svn3929
- add patch for upstream X.Org issue #25909
- add libXdmcp-devel to build requires to build Xvnc with XDMCP support (#552322)

* Mon Dec 21 2009 Adam Tkac <atkac redhat com> 1.0.90-0.1.20091221svn3929
- update to 1.0.90 snapshot
- patches merged
  - tigervnc10-compat.patch
  - tigervnc10-rh510185.patch
  - tigervnc10-rh524340.patch
  - tigervnc10-rh516274.patch

* Mon Oct 26 2009 Adam Tkac <atkac redhat com> 1.0.0-3
- create Xvnc keyboard mapping before first keypress (#516274)

* Thu Oct 08 2009 Adam Tkac <atkac redhat com> 1.0.0-2
- update underlying X source to 1.6.4-0.3.fc11
- remove bogus '-nohttpd' parameter from /etc/sysconfig/vncservers (#525629)
- initscript LSB compliance fixes (#523974)
- improve -LowColorSwitch documentation and handling (#510185)
- honor dotWhenNoCursor option (and it's changes) every time (#524340)

* Fri Aug 28 2009 Adam Tkac <atkac redhat com> 1.0.0-1
- update to 1.0.0
- tigervnc10-rh495457.patch merged to upstream

* Mon Aug 24 2009 Karsten Hopp <karsten@redhat.com> 0.0.91-0.17
- fix ifnarch s390x for server-module

* Fri Aug 21 2009 Tomas Mraz <tmraz@redhat.com> - 0.0.91-0.16
- rebuilt with new openssl

* Tue Aug 04 2009 Adam Tkac <atkac redhat com> 0.0.91-0.15
- make Xvnc compilable

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.91-0.14.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jul 13 2009 Adam Tkac <atkac redhat com> 0.0.91-0.13.1
- don't write warning when initscript is called with condrestart param (#508367)

* Tue Jun 23 2009 Adam Tkac <atkac redhat com> 0.0.91-0.13
- temporary use F11 Xserver base to make Xvnc compilable
- BuildRequires: libXi-devel
- don't ship tigervnc-server-module on s390/s390x

* Mon Jun 22 2009 Adam Tkac <atkac redhat com> 0.0.91-0.12
- fix local rendering of cursor (#495457)

* Thu Jun 18 2009 Adam Tkac <atkac redhat com> 0.0.91-0.11
- update to 0.0.91 (1.0.0 RC1)
- patches merged
  - tigervnc10-rh499401.patch
  - tigervnc10-rh497592.patch
  - tigervnc10-rh501832.patch
- after discusion in upstream drop tigervnc-bounds.patch
- configure flags cleanup

* Thu May 21 2009 Adam Tkac <atkac redhat com> 0.0.90-0.10
- rebuild against 1.6.1.901 X server (#497835)
- disable i18n, vncviewer is not UTF-8 compatible (#501832)

* Mon May 18 2009 Adam Tkac <atkac redhat com> 0.0.90-0.9
- fix vncpasswd crash on long passwords (#499401)
- start session dbus daemon correctly (#497592)

* Mon May 11 2009 Adam Tkac <atkac redhat com> 0.0.90-0.8.1
- remove merged tigervnc-manminor.patch

* Tue May 05 2009 Adam Tkac <atkac redhat com> 0.0.90-0.8
- update to 0.0.90

* Thu Apr 30 2009 Adam Tkac <atkac redhat com> 0.0.90-0.7.20090427svn3789
- server package now requires xorg-x11-fonts-misc (#498184)

* Mon Apr 27 2009 Adam Tkac <atkac redhat com> 0.0.90-0.6.20090427svn3789
- update to r3789
  - tigervnc-rh494801.patch merged
- tigervnc-newfbsize.patch is no longer needed
- fix problems when vncviewer and Xvnc run on different endianess (#496653)
- UltraVNC and TightVNC clients work fine again (#496786)

* Wed Apr 08 2009 Adam Tkac <atkac redhat com> 0.0.90-0.5.20090403svn3751
- workaround broken fontpath handling in vncserver script (#494801)

* Fri Apr 03 2009 Adam Tkac <atkac redhat com> 0.0.90-0.4.20090403svn3751
- update to r3751
- patches merged
  - tigervnc-xclients.patch
  - tigervnc-clipboard.patch
  - tigervnc-rh212985.patch
- basic RandR support in Xvnc (resize of the desktop)
- use built-in libjpeg (SSE2/MMX accelerated encoding on x86 platform)
- use Tight encoding by default
- use TigerVNC icons

* Tue Mar 03 2009 Adam Tkac <atkac redhat com> 0.0.90-0.3.20090303svn3631
- update to r3631

* Tue Mar 03 2009 Adam Tkac <atkac redhat com> 0.0.90-0.2.20090302svn3621
- package review related fixes

* Mon Mar 02 2009 Adam Tkac <atkac redhat com> 0.0.90-0.1.20090302svn3621
- initial package, r3621
