Summary: Utilities to query and test DNS
Name: bind-utils
Version: 9.11.19
Release: 1
License: MPLv2.0
URL: https://www.isc.org/downloads/bind/

Source: %{name}-%{version}.tar.gz

BuildRequires:  libtool
BuildRequires:  pkgconfig(openssl) < 3

%description
This package includes the utilities "host", "dig", and "nslookup" used to
test and query the Domain Name System (DNS). The Berkeley Internet
Name Domain (BIND) DNS server is found in the package named bind.

%prep
%autosetup -p1 -n %{name}-%{version}/bind9

%build
%reconfigure \
  --disable-static \
  --with-libtool \
  --without-libxml2 \
  --without-python
%make_build

%install

%make_install
%make_install -C bin/dig

rm -rf %{buildroot}/%{_mandir}
rm -rf %{buildroot}/usr/{sbin,include}
rm -rf %{buildroot}/etc
rm -rf %{buildroot}%{_bindir}/arpaname
rm -rf %{buildroot}%{_bindir}/bind9-config
rm -rf %{buildroot}%{_bindir}/delv
rm -rf %{buildroot}%{_bindir}/isc-config.sh
rm -rf %{buildroot}%{_bindir}/named-rrchecker
rm -rf %{buildroot}%{_libdir}/libirs.so*
rm -rf %{buildroot}%{_libdir}/libisccc.so*

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-, root, root, 0755)
%license LICENSE
%{_bindir}/dig
%{_bindir}/host
%{_bindir}/mdig
%{_bindir}/nslookup
%{_bindir}/nsupdate
%{_libdir}/*.so
%{_libdir}/*.so.*
