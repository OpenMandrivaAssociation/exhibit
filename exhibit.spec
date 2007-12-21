%define	name	exhibit
%define	version	0.0.1
%define release %mkrel 1

%define major 0
%define libname %mklibname %{name} %major
%define libnamedev %mklibname %{name} %major -d

Summary: 	Enlightenment image viewer
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
License: 	BSD
Group: 		Graphical desktop/Enlightenment
URL: 		http://get-e.org/
Source: 	%{name}-%{version}.tar.bz2
BuildRoot: 	%{_tmppath}/%{name}-buildroot
BuildRequires:	evas-devel >= 0.9.9.038, etk-devel >= 0.1.0.003
BuildRequires:	ecore-devel >= 0.9.9.038, edje-devel >= 0.5.0.038
BuildRequires:	epsilon-devel >= 0.3.0.008, engrave-devel >= 0.1.0
BuildRequires:	edje >= 0.5.0.038
Buildrequires:  flex
BuildRequires:  %{mklibname e0}-devel >= 0.16.999.038

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
