%define version          0.9.7
%define release          0
%define sourcename       check_bandwidth
%define packagename      nagios-plugins-check-bandwidth
%define nagiospluginsdir %{_libdir}/nagios/plugins

# No binaries in this package
%define debug_package    %{nil}

Summary:       A Nagios plugin to check if RedHat or Fedora system is up-to-date
Name:          %{packagename}
Version:       %{version}
Obsoletes:     check_bandwidth
Release:       %{release}%{?dist}
License:       GPLv3+
Packager:      Matteo Corti <matteo@corti.li>
Group:         Applications/System
BuildRoot:     %{_tmppath}/%{packagename}-%{version}-%{release}-root-%(%{__id_u} -n)
URL:           https://github.com/matteocorti/check_bandwidth
Source:        https://github.com/matteocorti/%{sourcename}/releases/download/v%{version}/%{sourcename}-%{version}.tar.gz

# Fedora build requirement (not needed for EPEL{4,5})
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Test::More)
BuildRequires: perl(Readonly)

Requires:      nagios-plugins
Requires:      iperf
# Yum security plugin RPM:
#    Fedora             : yum-plugin-security (virtual provides yum-security)
#    Red Hat Enterprise : yum-security
# Requires:  yum-security

%description
A Nagios plugin to check if RedHat or Fedora system is up-to-date

%prep
%setup -q -n %{sourcename}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor \
    INSTALLSCRIPT=%{nagiospluginsdir} \
    INSTALLVENDORSCRIPT=%{nagiospluginsdir}
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make pure_install PERL_INSTALL_ROOT=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} \;
find %{buildroot} -type f -name "*.pod" -exec rm -f {} \;
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null \;
%{_fixperms} %{buildroot}/*

%check
make test

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc AUTHORS Changes NEWS README TODO COPYING COPYRIGHT
%{nagiospluginsdir}/%{sourcename}
%{_mandir}/man3/%{sourcename}.3*

%changelog
* Tue Dec 24 2019 Matteo Corti <matteo@corti.li> - 0.9.7-0
- Updated to 0.9.7

* Fri Mar 21 2008 Matteo Corti <matteo.corti@id.ethz.ch> - 0.9.6-0
- fixed the usage message (wrong one)

* Fri Mar 21 2008 Matteo Corti <matteo.corti@id.ethz.ch> - 0.9.5-0
- fixed missing usage

* Thu Mar 20 2008 Matteo Corti <matteo.corti@id.ethz.ch> - 0.9.4-0
- ePN compatibility

* Wed Jan 23 2008 Matteo Corti <matteo.corti@id.ethz.ch> - 0.9.3-0
- updated to 0.9.3 (option to swap up- and downstream)

* Tue Jan 22 2008 Matteo Corti <matteo.corti@id.ethz.ch> - 0.9.2-0
- updated to 0.9.2 (options to specify local and remote ports)

* Fri Jan 18 2008 Matteo Corti <matteo.corti@id.ethz.ch> - 0.9.0-0
- Initial revision

