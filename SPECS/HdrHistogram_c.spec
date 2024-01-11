Name: HdrHistogram_c
Version: 0.9.13
Release: 2%{?dist}
Summary: C port of the HdrHistogram 
License: BSD and Public Domain
URL: https://github.com/HdrHistogram/%{name}
Source0: https://github.com/HdrHistogram/%{name}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires: gcc cmake zlib-devel

%description
C port of High Dynamic Range (HDR) Histogram.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -n %{name}-%{version}


%build
%cmake .
%make_build


%check
ls test
test/hdr_atomic_test
test/hdr_histogram_test


%install
rm -rf $RPM_BUILD_ROOT
%make_install
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'
find $RPM_BUILD_ROOT

%ldconfig_post

%ldconfig_postun


%files
%license LICENSE.txt
%doc README.md
%exclude %{_bindir}/hiccup
%exclude %{_bindir}/hdr_decoder
%exclude %{_bindir}/perftest
%exclude %{_bindir}/hdr_histogram_log_test
%exclude %{_bindir}/hdr_histogram_test
%exclude %{_bindir}/hdr_histogram_atomic_test
%{_libdir}/libhdr_histogram.so.5.0.0
%{_libdir}/libhdr_histogram.so.5
%exclude %{_libdir}/libhdr_histogram_static.a

%files devel
%dir %{_includedir}/hdr
%{_includedir}/hdr/hdr_thread.h
%{_includedir}/hdr/hdr_interval_recorder.h
%{_includedir}/hdr/hdr_writer_reader_phaser.h
%{_includedir}/hdr/hdr_time.h
%{_includedir}/hdr/hdr_histogram_log.h
%{_includedir}/hdr/hdr_histogram.h
%{_libdir}/libhdr_histogram.so

%changelog
* Wed May 20 2020 Nathan Scott <nathans@redhat.com> - 0.9.13-2
- Rebuild for CI/gating

* Wed Apr 29 2020 Nathan Scott <nathans@redhat.com> - 0.9.13-1
- Initial version for RHEL-8 (BZ 1748643)

* Wed Feb 12 2020 Lukas Zapletal <lzap+rpm@redhat.com> - 0.9.12-1
- New version

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Aug 14 2019 Lukáš Zapletal 0.9.11-1
- Initial package version
