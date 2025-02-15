%define	name	exhibit
%define	version	0.0.1
%define release %mkrel 5

%define major 0
%define libname %mklibname %{name} %major
%define libnamedev %mklibname %{name} %major -d

Summary: 	Enlightenment image viewer
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
License: 	BSD
Group: 		Graphical desktop/Enlightenment
URL: 		https://get-e.org/
Source: 	%{name}-%{version}.tar.bz2
BuildRoot: 	%{_tmppath}/%{name}-buildroot
BuildRequires:	evas-devel >= 0.9.9.050, etk-devel >= 0.1.0.042
BuildRequires:	ecore-devel >= 0.9.9.050, edje-devel >= 0.9.9.050
BuildRequires:	epsilon-devel >= 0.3.0.012, engrave-devel >= 0.1.0
BuildRequires:	edje >= 0.9.9.050
Buildrequires:  flex
BuildRequires:  e-devel >= 0.16.999.050
BuildRequires:  efreet-devel

%description
Exhibit is an image viewer powered by the EFL, in particular the new ETK
widget library. Its graphical user interface draws influences from GQview,
but there are also many new features, for example tabs.

This package is part of the Enlightenment DR17 desktop shell.

%prep
rm -rf $RPM_BUILD_ROOT
%setup -q

%build
./autogen.sh
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%{_bindir}/*
%{_datadir}/%name
