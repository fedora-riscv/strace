Summary: Tracks and displays system calls associated with a running process.
Name: strace
Version: 4.2
Release: 9
Copyright: distributable
Group: Development/Debuggers
URL: http://www.wi.leidenuniv.nl/~wichert/strace
Source0: http://www.liacs.nl/~wichert/strace/strace-%{version}.tar.gz
Patch0: strace-3.0.14elf.patch
Patch1: ftp://ftp.azstarnet.com/pub/linux/axp/glibc/strace-3.1-glibc.patch
Patch2: strace-3.1-sparc.patch
Patch3: strace-3.1-sparcglibc.patch
Patch4: strace-3.1-sparc2.patch
Patch5: strace-3.1-sparc3.patch
Patch6: strace-3.1-sparc4.patch
Patch7: strace-3.1-prctldomainname.patch
Patch8: strace-3.1-alpha.patch
Patch9: strace-3.1-gafton.patch
Patch10: strace-3.1-sparc5.patch
Patch11: strace-3.1-jbj.patch
Patch12: strace-3.1-arm.patch
Patch13: strace-3.1-compat21.patch
Patch14: strace-3.1-clone.patch
Patch15: strace-3.1-vfork.patch
Patch16: strace-3.1-jbj1.patch
Patch31: strace-3.99-sparc.patch

Patch50: strace-3.99-alphaosf.patch
Patch51: strace-3.99.1-seclvl.patch
Patch52: strace-3.99.1-sparc.patch
Patch53: strace-4.1-sparc.patch

Patch60: strace-4.2-ia64.patch
Patch61: strace-4.2-stat64.patch
Patch62: strace-4.2-sparc2.patch
Patch63: strace-4.2-putmsg.patch
Patch64: strace-4.2-newsysc.patch
Patch65: strace-4.2-getdents64.patch
Patch66: strace-4.2-sparc3.patch

BuildRoot: /var/tmp/%{name}-root
ExcludeArch: ia64

%description
The strace program intercepts and records the system calls called and
received by a running process.  Strace can print a record of each
system call, its arguments and its return value.  Strace is useful for
diagnosing problems and debugging, as well as for instructional
purposes.

Install strace if you need a tool to track the system calls made and
received by a process.

%prep
%setup -q

#%patch0 -p1 -b .elf
#%patch1 -p1 -b .glibc
#%patch2 -p1 -b .sparc
#%patch3 -p1 -b .sparcglibc
#%patch4 -p1 -b .sparc2
#%patch5 -p1 -b .sparc3
#%patch6 -p1 -b .sparc4
#%patch7 -p1 -b .misc
#%patch8 -p1 -b .alpha
#%patch9 -p1 -b .gafton
#%patch10 -p1 -b .sparc5
#%patch11 -p1 -b .jbj
#%patch12 -p1 -b .arm
#%patch13 -p1 -b .compat21
#%patch14 -p0 -b .clone
#%patch15 -p1 -b .vfork
#%patch16 -p1 -b .jbj1

#%patch31 -p1 -b .sparc

#%patch50 -p1
#%patch51 -p1
#%patch52 -p1
%patch53 -p1 -b .sparc

%patch60 -p1 -b .ia64
%patch61 -p1 -b .stat64
%patch62 -p1 -b .sparc2
%patch63 -p1 -b .putmsg
%patch64 -p1 -b .newsysc
%patch65 -p1 -b .getdents64
%patch66 -p1 -b .sparc3

%build
libtoolize --copy --force
aclocal
autoheader
autoconf

#OS=`echo ${RPM_OS} | tr '[A-Z]' '[a-z]'`
#CFLAGS="$RPM_OPT_FLAGS" ./configure --prefix=/usr ${RPM_ARCH}-redhat-${OS}

%configure
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p ${RPM_BUILD_ROOT}%{_mandir}/man1
mkdir -p ${RPM_BUILD_ROOT}%{_prefix}/bin
%makeinstall man1dir=${RPM_BUILD_ROOT}%{_mandir}/man1
strip ${RPM_BUILD_ROOT}%{_prefix}/bin/strace

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_prefix}/bin/strace
%{_mandir}/man1/strace.1*

%changelog
* Sat Aug 19 2000 Jakub Jelinek <jakub@redhat.com>
- doh, actually apply the 2.4 syscalls patch
- make it compile with 2.4.0-test7-pre4+ headers, add
  getdents64 and fcntl64

* Thu Aug  3 2000 Jakub Jelinek <jakub@redhat.com>
- add a bunch of new 2.4 syscalls (#14036)

* Wed Jul 12 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild
- excludearch ia64

* Fri Jun  2 2000 Matt Wilson <msw@redhat.com>
- use buildinstall for FHS

* Wed May 24 2000 Jakub Jelinek <jakub@redhat.com>
- make things compile on sparc
- fix sigreturn on sparc

* Fri Mar 31 2000 Bill Nottingham <notting@redhat.com>
- fix stat64 misdef (#10485)

* Tue Mar 21 2000 Michael K. Johnson <johnsonm@redhat.com>
- added ia64 patch

* Thu Feb 03 2000 Cristian Gafton <gafton@redhat.com>
- man pages are compressed
- version 4.2 (why are we keeping all these patches around?)

* Sat Nov 27 1999 Jeff Johnson <jbj@redhat.com>
- update to 4.1 (with sparc socketcall patch).

* Fri Nov 12 1999 Jakub Jelinek <jakub@redhat.com>
- fix socketcall on sparc.

* Thu Sep 02 1999 Cristian Gafton <gafton@redhat.com>
- fix KERN_SECURELVL compile problem

* Tue Aug 31 1999 Cristian Gafton <gafton@redhat.com>
- added alpha patch from HJLu to fix the osf_sigprocmask interpretation

* Sat Jun 12 1999 Jeff Johnson <jbj@redhat.com>
- update to 3.99.1.

* Wed Jun  2 1999 Jeff Johnson <jbj@redhat.com>
- add (the other :-) jj's sparc patch.

* Wed May 26 1999 Jeff Johnson <jbj@redhat.com>
- upgrade to 3.99 in order to
-    add new 2.2.x open flags (#2955).
-    add new 2.2.x syscalls (#2866).
- strace 3.1 patches carried along for now.

* Sun May 16 1999 Jeff Johnson <jbj@redhat.com>
- don't rely on (broken!) rpm %patch (#2735)

* Tue Apr 06 1999 Preston Brown <pbrown@redhat.com>
- strip binary

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 16)

* Tue Feb  9 1999 Jeff Johnson <jbj@redhat.com>
- vfork est arrive!

* Tue Feb  9 1999 Christopher Blizzard <blizzard@redhat.com>
- Add patch to follow clone() syscalls, too.

* Sun Jan 17 1999 Jeff Johnson <jbj@redhat.com>
- patch to build alpha/sparc with glibc 2.1.

* Thu Dec 03 1998 Cristian Gafton <gafton@redhat.com>
- patch to build on ARM

* Wed Sep 30 1998 Jeff Johnson <jbj@redhat.com>
- fix typo (printf, not tprintf).

* Sat Sep 19 1998 Jeff Johnson <jbj@redhat.com>
- fix compile problem on sparc.

* Tue Aug 18 1998 Cristian Gafton <gafton@redhat.com>
- buildroot

* Mon Jul 20 1998 Cristian Gafton <gafton@redhat.com>
- added the umoven patch from James Youngman <jay@gnu.org>
- fixed build problems on newer glibc releases

* Mon Jun 08 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr
