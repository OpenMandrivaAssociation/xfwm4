Summary:	Window manager for Xfce desktop environment
Name:		xfwm4
Version: 	4.6.0
Release:	%mkrel 3
License:	GPLv2+
Group:		Graphical desktop/Xfce
URL:		http://www.xfce.org
Source0:	http://www.xfce.org/archive/xfce-%{version}/src/%{name}-%{version}.tar.bz2
Patch0:		xfwm4-4.6.0-reduce-repaint-timeout-in-the-compositor.patch
Patch1:		xfwm4-4.6.0-check-for-nil-timestamp-regardless-of-focus-stealing-prevention-setting.patch
Patch2:		xfwm4-4.6.0-reduce-minimum-timeout-for-focus-delay-in-focus-follow-mouse.patch
Patch3:		xfwm4-4.6.0-regrab-the-mouse-on-parent-window.patch
Patch4:		xfwm4-4.6.0-do-not-not-fill-over-adjacent-windows.patch
Patch5:		xfwm4-4.6.0-keep-window-layer-when-status-is-above-below-or-fullscreen.patch
BuildRequires:	libgdk_pixbuf2.0-devel
BuildRequires:	libxcomposite-devel
BuildRequires:	libxdamage-devel
BuildRequires:	startup-notification-devel
BuildRequires:	libxfcegui4-devel >= %{version}
BuildRequires:	xfconf-devel >= %{version}
BuildRequires:	libglade2-devel
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
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

%build
%configure2_5x \
%if %mdkversion < 200900
	--sysconfdir=%{_sysconfdir}/X11 \
%endif
	--enable-compositor \
	--enable-xsync \
	--enable-render \
	--enable-randr \
	--enable-startup-notification \
	--disable-static
%make

%install
rm -rf %{buildroot}

%makeinstall_std

%find_lang %{name}

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post
%{update_menus}
%update_icon_cache hicolor
%endif

%if %mdkversion < 200900
%postun
%{clean_menus}
%clean_icon_cache hicolor
%endif

%files -f %{name}.lang
%defattr(-,root,root)
%doc example.gtkrc-2.0 AUTHORS COMPOSITOR README TODO
%dir %{_libdir}/xfce4/xfwm4
%{_bindir}/xfwm4*
%{_libdir}/xfce4/xfwm4/helper-dialog
%{_datadir}/applications/*
%{_iconsdir}/hicolor/*
%{_datadir}/themes/*
%{_datadir}/xfwm4
%{_datadir}/xfce4/doc
