Summary:	Window manager for Xfce desktop environment
Name:		xfwm4
Version: 	4.4.2
Release:	%mkrel 4
License:	GPLv2+
Group:		Graphical desktop/Xfce
URL:		http://www.xfce.org
Source0:	%{name}-%{version}.tar.bz2
Patch0:		%{name}-4.4.2-filter-ungrab-events.patch
Patch1:		%{name}-4.4.2-exit-on-selectionclear.patch
Patch2:		%{name}-4.4.2-fix-compositing-overlay.patch
Patch3:		%{name}-4.4.2-fix-automaximize-on-move.patch
Patch4:		%{name}-4.4.2-awn-focus.patch
BuildRequires:	xfce-mcs-manager-devel >= %{version}
BuildRequires:	libgdk_pixbuf2.0-devel
BuildRequires:	libxcomposite-devel
BuildRequires:	libxdamage-devel
BuildRequires:	startup-notification-devel
Requires:	xfce-mcs-manager >= %{version}
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

%build
%configure2_5x \
%if %mdkversion < 200900
	--sysconfdir=%{_sysconfdir}/X11 \
%endif
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
%doc example.gtkrc-2.0 AUTHORS COMPOSITOR README TODO
%{_bindir}/xfwm4
%{_libdir}/xfce4/mcs-plugins/*
%{_datadir}/applications/*
%{_iconsdir}/hicolor/*
%{_datadir}/themes/*
%{_datadir}/xfwm4
%{_datadir}/xfce4/doc
