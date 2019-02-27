Name: geoclue-provider-hybris-binder
Provides: geoclue-provider-hybris = %{version}
Conflicts: geoclue-provider-hybris <= 0.2.21
Conflicts: geoclue-provider-hybris-hal
Obsoletes: geoclue-provider-hybris < %{version}

# libgbinder is currently not a common package, so we have to rely on tar_git.
BuildRequires: pkgconfig(libgbinder)

# hardcoded build command, can be autodetected
%define qmake_command qmake -qt=5 binder/binderlocationbackend.pro

%include rpm/geoclue-providers-hybris.inc

