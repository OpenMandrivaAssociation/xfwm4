Summary:	Window manager for Xfce
Name:		xfwm4
Version: 	4.4.2
Release:	%mkrel 1
License:	GPLv2+
Group:		Graphical desktop/Xfce
URL:		http://www.xfce.org
Source0:	%{name}-%{version}.tar.bz2
Requires:	xfce-mcs-manager >= %{version}
BuildRequires:	xfce-mcs-manager-devel >= %{version}
BuildRequires:	libgdk_pixbuf2.0-devel
BuildRequires:	libxcomposite-devel
BuildRequires:	libxdamage-devel
BuildRequires:	startup-notification-devel
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
	--sysconfdir=%{_sysconfdir}/X11 \
	--enable-compositor \
	--enable-xsync \
	--enable-render \
	--enable-randr \
	--disable-static
%make

%install
rm -rf %{buildroot}

%makeinstall_std

%find_lang %{name}

%clean
rm -rf %{buildroot}

%post
%{update_menus}
%update_icon_cache hicolor

%postun
%{clean_menus}
%clean_icon_cache hicolor

%files -f %{name}.lang
%defattr(-,root,root)
%doc example.gtkrc-2.0 AUTHORS COMPOSITOR COPYING README TODO
%{_bindir}/xfwm4
%{_libdir}/xfce4/mcs-plugins/*
%{_datadir}/applications/*
%{_iconsdir}/hicolor/*
%{_datadir}/themes/*
%{_datadir}/xfwm4
%{_datadir}/xfce4/doc
