%define url_ver %(echo %{version} | cut -d. -f1,2)
%define _disable_rebuild_configure 1

Summary:	Window manager for Xfce desktop environment
Name:		xfwm4
Version: 	4.12.5
Release:	2
License:	GPLv2+
Group:		Graphical desktop/Xfce
URL:		http://www.xfce.org
Source0:	http://archive.xfce.org/src/xfce/xfwm4/%{url_ver}/%{name}-%{version}.tar.bz2
BuildRequires:	pkgconfig(gdk-pixbuf-2.0)
BuildRequires:	pkgconfig(xcomposite)
BuildRequires:	pkgconfig(xdamage)
BuildRequires:	pkgconfig(libstartup-notification-1.0)
BuildRequires:	pkgconfig(libxfce4ui-1) >= 4.12
BuildRequires:	pkgconfig(libxfconf-0) >= 4.12
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

%files -f %{name}.lang
%doc example.gtkrc-2.0 AUTHORS COMPOSITOR README TODO
%dir %{_libdir}/xfce4/xfwm4
%{_bindir}/xfwm4*
%{_libdir}/xfce4/xfwm4/helper-dialog
%{_datadir}/applications/*
%{_iconsdir}/hicolor/*
%{_datadir}/themes/*
%{_datadir}/xfwm4

#---------------------------------------------------------------------------

%prep
%setup -q
%autopatch -p1

%build
%configure \
	--enable-compositor \
	--enable-xsync \
	--enable-render \
	--enable-randr \
	--enable-startup-notification \
	%{nil}
%make_build

%install
%make_install

# locales
%find_lang %{name} %{name}.lang
