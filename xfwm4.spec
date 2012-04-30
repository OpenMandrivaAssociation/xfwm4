%define url_ver %(echo %{version} | cut -c 1-3)

Summary:	Window manager for Xfce desktop environment
Name:		xfwm4
Version: 	4.10.0
Release:	1
License:	GPLv2+
Group:		Graphical desktop/Xfce
URL:		http://www.xfce.org
Source0:	http://archive.xfce.org/src/xfce/%{name}/%{url_ver}/%{name}-%{version}.tar.bz2
BuildRequires:	libgdk_pixbuf2.0-devel
BuildRequires:	libxcomposite-devel
BuildRequires:	libxdamage-devel
BuildRequires:	startup-notification-devel
BuildRequires:	libxfce4ui-devel >= 4.9.1
BuildRequires:	xfconf-devel >= 4.9.0
BuildRequires:	libglade2.0-devel
BuildRequires:	libwnck-devel
Obsoletes:	xfwm
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

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
