Summary: Utilities to query and test DNS
Name: bind-utils
Version: 9.11.19
Release: 1
License: MPLv2.0
URL: https://www.isc.org/downloads/bind/

Source: %{name}-%{version}.tar.gz

BuildRequires:  libtool
BuildRequires:  openssl-devel

%description
This package includes the utilities "host", "dig", and "nslookup" used to
test and query the Domain Name System (DNS). The Berkeley Internet
Name Domain (BIND) DNS server is found in the package named bind.

%prep
%autosetup -p1 -n %{name}-%{version}/bind9

%build
%reconfigure \
  --with-libtool \
  --without-python
make %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}

%make_install
make DESTDIR=%{buildroot} -C bin/dig install

%{__rm} -rf %{buildroot}/%{_mandir}
%{__rm} -rf %{buildroot}/usr/{sbin,include}
%{__rm} -rf %{buildroot}/etc
%{__rm} -rf %{buildroot}%{_bindir}/arpaname
%{__rm} -rf %{buildroot}%{_bindir}/bind9-config
%{__rm} -rf %{buildroot}%{_bindir}/delv
%{__rm} -rf %{buildroot}%{_bindir}/isc-config.sh
%{__rm} -rf %{buildroot}%{_bindir}/named-rrchecker
%{__rm} -rf %{buildroot}%{_libdir}/libirs.so*
%{__rm} -rf %{buildroot}%{_libdir}/libisccc.so*

%clean
%{__rm} -rf %{buildroot}

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

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
