Summary: Tracks and displays system calls associated with a running process.
Name: strace
Version: 4.3
Release: 2
License: BSD
Group: Development/Debuggers
URL: http://sourceforge.net/projects/strace/
Source0: %{name}-%{version}.tar.gz
Patch1: strace-4.2-sparc.patch
Patch3: strace-4.2-sparc2.patch
Patch4: strace-4.2-putmsg.patch
#Patch5: strace-4.2-newsysc.patch
#Patch6: strace-4.2-getdents64.patch
Patch7: strace-4.2-sparc3.patch
Patch8: strace-4.2.2-s390.patch
Patch9: strace-4.3-ia64.patch
Patch10: strace-4.2-sparc4.patch
Patch11: strace-4.2.2-include.patch
BuildRoot: %{_tmppath}/%{name}-root
BuildPrereq: autoconf

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
%patch4 -p1 -b .putmsg

#%ifnarch s390
#%patch5 -p1 -b .newsysc
#%patch6 -p1 -b .getdents64
#%endif

#%ifarch s390 s390x
#%patch8 -p1 -b .s390
#%endif

%ifarch ia64
%patch9 -p1 -b .ia64
%endif

%ifarch sparc sparc64
%patch1 -p1 -b .sparc
%patch3 -p1 -b .sparc2
%patch7 -p1 -b .sparc3
%patch10 -p1 -b .sparc4
%endif

%patch11 -p1 -b .incl

%build
./cvsbuild
%configure
make

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_mandir}/man1
mkdir -p %{buildroot}%{_bindir}
%makeinstall man1dir=%{buildroot}%{_mandir}/man1

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/strace
%{_mandir}/man1/*

%changelog
* Sun Jul 22 2001 Florian La Roche <Florian.LaRoche@redhat.de>
- disable s390 patches, they are already included

* Wed Jul 18 2001 Preston Brown <pbrown@redhat.com> 4.3-1
- new upstream version.  Seems to have integrated most new syscalls
- tracing threaded programs is now functional.

* Mon Jun 11 2001 Than Ngo <than@redhat.com>
- port s390 patches from IBM

* Wed May 16 2001 Nalin Dahyabhai <nalin@redhat.com>
- modify new syscall patch to allocate enough heap space in setgroups32()

* Wed Feb 14 2001 Jakub Jelinek <jakub@redhat.com>
- #include <time.h> in addition to <sys/time.h>

* Fri Jan 26 2001 Karsten Hopp <karsten@redhat.com>
- clean up conflicting patches. This happened only
  when building on S390

* Fri Jan 19 2001 Bill Nottingham <notting@redhat.com>
- update to CVS, reintegrate ia64 support

* Sat Dec  8 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- Get S/390 support into the normal package

* Sat Nov 18 2000 Florian La Roche <Florian.LaRoche@redhat.de>
- added S/390 patch from IBM, adapting it to not conflict with
  IA64 patch

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
