%define	name	openmoko-libs
%define	version	0
%define	svnrel	20070709
%define	release %mkrel 0.%{svnrel}.1

%define major	0
%define libname %mklibname moko %{major}
%define	devname	%mklibname -d moko

Summary: 	Libraries for OpenMoko
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
Group: 		System/Libraries
License: 	LGPL
URL: 		http://www.openmoko.org/
Source0:	%{name}-%{svnrel}.tar.lzma
BuildRequires:	lzma gsmd-devel evolution-data-server-devel gtk+-devel
BuildRequires:	pango-devel atk-devel xosd-devel

%description
Libraries for OpenMoko.

%package -n	%{libname}
Summary:	Libraries for OpenMoko
Group:		System/Libraries
Provides:	%{name} = %{version}-%{release}

%description -n	%{libname}
Libraries for OpenMoko.

%package -n	%{devname}
Summary:	Development files for %{name}
Group:		Development/C
License:	LGPL
Requires:	%{libname} = %{version}
Provides:	%{name}-devel = %{version}

%description -n	%{devname}
Development files for %{name}.

%prep
%setup -q -n %{name}

%build
autoreconf -v --install
glib-gettextize --force --copy
%configure --disable-static
%make

%install
rm -rf %{buildroot}
%makeinstall
rm -f %{buildroot}%{_libdir}/{,gsmd/}*.la

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%clean
rm -rf %{buildroot}

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/*.so.*

%files -n %{devname}
%defattr(-,root,root)
%dir %{_includedir}/%{name}
%dir %{_includedir}/%{name}/libmokogsmd
%{_includedir}/%{name}/libmokogsmd/*.h
%dir %{_includedir}/%{name}/libmokojournal
%{_includedir}/%{name}/libmokojournal/*.h
%dir %{_includedir}/%{name}/libmokoui
%{_includedir}/%{name}/libmokoui/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/%{name}.pc
