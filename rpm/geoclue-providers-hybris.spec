Version: 0.0.1
Release: 1
Name: geoclue-provider-hybris-hal
Provides: geoclue-provider-hybris = %{version}-%{release}
Conflicts: geoclue-provider-hybris <= 0.2.21
Conflicts: geoclue-provider-hybris-binder
Obsoletes: geoclue-provider-hybris < %{version}-%{release}

BuildRequires: pkgconfig(libhardware)
BuildRequires: pkgconfig(android-headers)

# hardcoded build command, can be autodetected
%define qmake_command qmake -qt=5 hal/hallocationbackend.pro

%include rpm/geoclue-providers-hybris.inc

