Name: geoclue-provider-hybris
Version: 0.0.1
Release: 1
Summary: Geoinformation Service Hybris Provider
Group: System/Libraries
URL: https://bitbucket.org/jolla/base-geoclue-providers-hybris
License: Proprietary
Source: %{name}-%{version}.tar.gz
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5DBus)
BuildRequires: pkgconfig(libhardware)
BuildRequires: pkgconfig(android-headers)

%description
%{summary}.


%prep
%setup -q -n %{name}-%{version}


%build
qmake -qt=5
make %{?_smp_mflags}


%install
make INSTALL_ROOT=%{buildroot} install

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%{_libexecdir}/geoclue-hybris
%{_datadir}/dbus-1/services/org.freedesktop.Geoclue.Providers.Hybris.service
%{_datadir}/geoclue-providers/geoclue-hybris.provider
