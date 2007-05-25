%define	name	exhibit
%define	version	0.0.1
%define release 0.%{cvsrel}.1mdk

%define cvsrel 20060323

%define major 	0
%define libname %mklibname %{name} %major
%define libnamedev %mklibname %{name} %major -d

Summary: 	Enlightenment image viewer
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
License: 	BSD
Group: 		Graphical desktop/Enlightenment
URL: 		http://get-e.org/
Source: 	%{name}-%{cvsrel}.tar.bz2
BuildRoot: 	%{_tmppath}/%{name}-buildroot
BuildRequires:	evas-devel etk-devel
BuildRequires:	ecore-devel edje-devel 
BuildRequires:	epsilon-devel e-devel engrave-devel
BuildRequires:	edje

%description
Exhibit is an image viewer powered by the EFL, in particular the new ETK
widget library. Its graphical user interface draws influences from GQview,
but there are also many new features, for example tabs.

This package is part of the Enlightenment DR17 desktop shell.

%prep
rm -rf $RPM_BUILD_ROOT
%setup -q -n %name

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
