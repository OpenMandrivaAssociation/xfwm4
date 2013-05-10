%define url_ver %(echo %{version} | cut -c 1-4)

Summary:	Window manager for Xfce desktop environment
Name:		xfwm4
Version: 	4.10.1
Release:	1
License:	GPLv2+
Group:		Graphical desktop/Xfce
URL:		http://www.xfce.org
Source0:	http://archive.xfce.org/src/xfce/%{name}/%{url_ver}/%{name}-%{version}.tar.bz2
BuildRequires:	pkgconfig(gdk-pixbuf-2.0)
BuildRequires:	pkgconfig(xcomposite)
BuildRequires:	pkgconfig(xdamage)
BuildRequires:	pkgconfig(libstartup-notification-1.0)
BuildRequires:	pkgconfig(libxfce4ui-1) >= 4.9.1
BuildRequires:	pkgconfig(libxfconf-0) >= 4.9.0
BuildRequires:	pkgconfig(libglade-2.0)
BuildRequires:	pkgconfig(libwnck-1.0)
Obsoletes:	xfwm

%description
The Xfce 4 window manager manages the placement of application
windows on the screen, provides beautiful window decorations,
manages workspaces or virtual desktops, and natively supports
multiscreen mode. It provides its own compositing manager (
from the Xorg Composite extension) for true transparency and shadows.
The Xfce 4 window manager includes a keyboard shorcuts editor for user
specific commands and basic windows manipulations, and it provides a
dialog for advanced tweaks.

%prep
%setup -q

%build
%configure2_5x \
	--enable-compositor \
	--enable-xsync \
	--enable-render \
	--enable-randr \
	--enable-startup-notification \
	--disable-static

%make

%install
%makeinstall_std

%find_lang %{name} %{name}.lang

%files -f %{name}.lang
%doc example.gtkrc-2.0 AUTHORS COMPOSITOR README TODO
%dir %{_libdir}/xfce4/xfwm4
%{_bindir}/xfwm4*
%{_libdir}/xfce4/xfwm4/helper-dialog
%{_datadir}/applications/*
%{_iconsdir}/hicolor/*
%{_datadir}/themes/*
%{_datadir}/xfwm4


%changelog
* Tue May 01 2012 Tomasz Pawel Gajc <tpg@mandriva.org> 4.10.0-1
+ Revision: 794661
- update to new version 4.10.0

* Sun Apr 15 2012 Tomasz Pawel Gajc <tpg@mandriva.org> 4.9.1-1
+ Revision: 791061
- update to new version 4.9.1

* Thu Apr 05 2012 Tomasz Pawel Gajc <tpg@mandriva.org> 4.9.0-1
+ Revision: 789478
- update to new version 4.9.0
- drop old stuff from spec file

* Wed Dec 21 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 4.8.3-1
+ Revision: 744192
- update to new version 4.8.3

* Sun Nov 20 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 4.8.2-2
+ Revision: 732068
- fix br
- rebuild for glib2

* Fri Sep 23 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 4.8.2-1
+ Revision: 701026
- update to new version 4.8.2

* Sat Mar 12 2011 Funda Wang <fwang@mandriva.org> 4.8.1-2
+ Revision: 643891
- rebuild to obsolete old packages

* Wed Feb 02 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 4.8.1-1
+ Revision: 635014
- update to new version 4.8.1

* Sun Jan 23 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 4.8.0-1
+ Revision: 632413
- update to new version 4.8.0

* Thu Jan 06 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 4.7.4-1mdv2011.0
+ Revision: 629130
- update to new version 4.7.4

* Wed Dec 08 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 4.7.3-1mdv2011.0
+ Revision: 616366
- update to new version 4.7.3

* Thu Dec 02 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 4.7.2-1mdv2011.0
+ Revision: 605587
- update to new version 4.7.2
- bump minimum requirements on libxfce4ui to 4.7.5 version

* Sat Nov 06 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 4.7.1-1mdv2011.0
+ Revision: 593834
- update to new version 4.7.1

* Sat Sep 18 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 4.7.0-1mdv2011.0
+ Revision: 579389
- update to new version 4.7.0
- adjust buildrequires
- fix file list

* Fri Jul 16 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 4.6.2-1mdv2011.0
+ Revision: 553896
- update to new version 4.6.2

* Fri May 07 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 4.6.1-2mdv2010.1
+ Revision: 543223
- rebuild for mdv 2010.1

* Tue Apr 21 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 4.6.1-1mdv2010.0
+ Revision: 368582
- update to new version 4.6.1

* Mon Apr 06 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 4.6.0-4mdv2009.1
+ Revision: 364408
- Patch6: Check fullscreen status against each monitor

* Sun Apr 05 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 4.6.0-3mdv2009.1
+ Revision: 364220
- Patch0: reduce repain timeout in the compositor
- Patch1: check for nil timestamp regardless of focus stealing prevention setting
- Patch2: reduce minimum timeout for focus delay in focus follow mouse
- Patch3: regrab the mouse on parent window
- Patch4: do not not fill over adjacent windows

* Thu Mar 05 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 4.6.0-2mdv2009.1
+ Revision: 349264
- rebuild whole xfce

* Fri Feb 27 2009 Jérôme Soyer <saispo@mandriva.org> 4.6.0-1mdv2009.1
+ Revision: 345703
- New upstream release

* Mon Jan 26 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 4.5.99.1-1mdv2009.1
+ Revision: 333925
- update to new version 4.5.99.1

* Wed Jan 14 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 4.5.93-1mdv2009.1
+ Revision: 329525
- update to new version 4.5.93
- add full path for the Source0

* Sat Nov 15 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 4.5.92-1mdv2009.1
+ Revision: 303496
- update to new version 4.5.92 (Xfce 4.6 Beta 2 Hopper)
- versionate buildrequires

* Fri Oct 17 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 4.5.91-1mdv2009.1
+ Revision: 294524
- Xfce4.6 beta1 is landing on cooker
- drop all patches as they were merged by upstream
- tune up buildrequires
- fix file list

* Sat Aug 09 2008 Thierry Vignaud <tv@mandriva.org> 4.4.2-5mdv2009.0
+ Revision: 269799
- rebuild early 2009.0 package (before pixel changes)

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Mon May 19 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 4.4.2-4mdv2009.0
+ Revision: 209019
- reorder patches
- Patch1: filter ungrab events
- Patch2: exit on selectionclear
- Patch3: fix compositing overlay
- Patch4: fix automaximize on move

* Sun May 11 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 4.4.2-3mdv2009.0
+ Revision: 205606
- change sysconfdir from /etc/X11/xdg to /etc/xdg only for Mandriva releases newer than 2008.1

* Wed Mar 19 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 4.4.2-2mdv2008.1
+ Revision: 189000
- Patch0: fix focus problems with avant-window-navigator
- remove COPYING file from docs

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sun Nov 18 2007 Jérôme Soyer <saispo@mandriva.org> 4.4.2-1mdv2008.1
+ Revision: 109994
- Remove unneeded patch
- New release 4.4.2

  + Tomasz Pawel Gajc <tpg@mandriva.org>
    - new license policy
    - use upstream tarball name as a real name
    - use upstream name

* Sat Sep 22 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 4.4.1-9mdv2008.0
+ Revision: 92282
- provide patch 4, which fixes upstream Xfce bug #3296

* Fri Sep 21 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 4.4.1-8mdv2008.0
+ Revision: 91888
- drop patch 1 because it does nothing :(

* Sat Aug 25 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 4.4.1-7mdv2008.0
+ Revision: 71392
- provide patch 3 (fix against gtk 2.11.x which kills keyboard/mouse events)
- some cleans
- SILET remove it

* Tue Jun 26 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 4.4.1-6mdv2008.0
+ Revision: 44314
- disable compiling of static files rather than deleting them

* Mon Jun 04 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 4.4.1-5mdv2008.0
+ Revision: 35021
- provide P2 (fix memory leak)
- update description
- provide patch0

* Tue May 29 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 4.4.1-4mdv2008.0
+ Revision: 32565
- use macros in %%post and %%postun
- drop Source1
- drop __libtoolize
- add configure options
- spec file clean

* Thu Apr 26 2007 Herton Ronaldo Krzesinski <herton@mandriva.com.br> 4.4.1-3mdv2008.0
+ Revision: 18426
- Oops, forgot to bump release in last commit.
- Added missing BuildRequires for libxcomposite-devel and
  libxdamage-devel when building with compositor.

* Wed Apr 25 2007 Jérôme Soyer <saispo@mandriva.org> 4.4.1-2mdv2008.0
+ Revision: 18232
- Build with compositor by default

* Mon Apr 23 2007 Jérôme Soyer <saispo@mandriva.org> 4.4.1-1mdv2008.0
+ Revision: 17695
- New release 4.4.1

