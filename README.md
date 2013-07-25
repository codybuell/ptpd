Precision Time Protocol (PTP)
=============================

Spec and sources to build ptpd rpms.

Current version: 2.2.2

PTPd Overview
-------------

The PTP daemon (PTPd) implements the Precision Time protocol (PTP) as defined
by the relevant IEEE 1588 standard. PTP Version 1 implements IEEE-1588-2002,
and PTP Version 2 implements IEEE-1588-2008. PTP was developed to provide very
precise time coordination of LAN connected computers.

PTPd is a complete implementation of the IEEE 1588 specification for a standard
(non-boundary) clock. PTPd has been tested with and is known to work properly
with other IEEE 1588 implementations. The source code for PTPd is freely
available under a BSD-style license. Thanks to contributions from users, PTPd
is becoming an increasingly portable, interoperable, and stable IEEE 1588
implementation.

PTPd can run on most 32-bit or 64-bit, little- or big-endian processors. It
does not require an FPU, so it is great for embedded processors. PTPd currently
runs on Linux, uClinux, FreeBSD, and NetBSD. It should also be easy to port to
other platforms.

PTPd is free. Everyone is welcome to use and contribute to PTPd.

<cite>Taken from <http://ptpd.sourceforge.net/></cite>

Usage
-----

1. Setup the rpm build environment.

        # install required packages
        yum -y install gcc make rpm-build redhat-rpm-config

        # create rpmbuild user account
        useradd -d /home/rpmbuild -m -s /bin/bash rpmbuild

        # create .rpmmacros file
        echo '%_topdir     %(echo $HOME)/rpmbuild' > /home/rpmbuild/.rpmmacros
        echo '%_tmppath    %(echo $HOME)/rpmbuild/TMP' >> /home/rpmbuild/.rpmmacros
        chown rpmbuild:rpmbuild /home/rpmbuild/.rpmmacros
        chmod 644 /home/rpmbuild/.rpmmacros

        # create build directory structure
        mkdir -p /home/rpmbuild/rpmbuild/{BUILD,RPMS,SOURCES,SPECS,SRPMS,TMP} 
        chown -R rpmbuild:rpmbuild /home/rpmbuild/rpmbuild
        chmod -R 755 /home/rpmbuild/rpmbuild

2. Copy spec and sources to rpmbuild directories.

3. Build the rpm.

        su - rpmbuild
        cd rpmbuild/SPECS
        rpmbuild -ba ptpd.spec
