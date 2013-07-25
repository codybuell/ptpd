################################################################################
#                                                                              #
#                                   PTPD Spec                                  #
#                                                                              #
################################################################################

Summary   : The PTP daemon to implement IEEE 1588v1 Precision Time Protocol (PTP)
Name      : ptpd
Version   : 2.2.2
Release   : 0
License   : BSD
Packager  : Cody Buell (cody.buell@nasa.gov)
Group     : System Environment/Daemons
URL       : http://downloads.sourceforge.net/project/ptpd/ptpd/2.2.2/ptpd-2.2.2.tar.gz
Source0   : %{name}-%{version}.tar.gz
Source1   : %{name}2.init
Source2   : %{name}2.conf
Source3   : %{name}2.logrotate
BuildRoot : %{_tmppath}/%{name}

%description
The PTP daemon (PTPd) implements the Precision Time protocol (PTP) as defined
by the IEEE 1588 standard. PTP was developed to provide very precise time
coordination of LAN connected computers.

PTPd is a complete implementation of the IEEE 1588 specification for a standard
(non-boundary) clock. PTPd has been tested with and is known to work properly
with other IEEE 1588 implementations. The source code for PTPd is freely
available under a BSD-style license. Thanks to contributions from users, PTPd
is becoming an increasingly portable, interoperable, and stable IEEE 1588
implementation.

PTPd can run on most 32-bit little- or big-endian processors. It does not
require an FPU, so it is great for embedded processors. PTPd currently runs on
Linux, uClinux, FreeBSD, and NetBSD. It should also be easy to port to other
platforms.

PTPd is free. Everyone is invited to use and contribute to PTPd.

%prep
# clearn up old build trees, uncompress and extract source
%setup

%build
cd src
make all

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT/usr/sbin
mkdir -p $RPM_BUILD_ROOT/etc/init.d
mkdir -p $RPM_BUILD_ROOT/etc/sysconfig
mkdir -p $RPM_BUILD_ROOT/etc/logrotate.d

cp -a src/ptpd2 $RPM_BUILD_ROOT/usr/sbin
install -m 755 %{S:1} $RPM_BUILD_ROOT/etc/init.d/ptpd2
install -m 644 %{S:2} $RPM_BUILD_ROOT/etc/sysconfig/ptpd2
install -m 644 %{S:3} $RPM_BUILD_ROOT/etc/logrotate.d/ptpd2

%pre

%post
/sbin/chkconfig --add %{name}2

%files
%defattr(-,root,root)
/usr/sbin/ptpd2
/etc/init.d/ptpd2
/etc/sysconfig/ptpd2
/etc/logrotate.d/ptpd2

%clean
rm -rf $RPM_BUILD_ROOT
