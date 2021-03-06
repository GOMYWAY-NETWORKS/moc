# Filtering of private libraries
%global __provides_exclude_from ^%{_libdir}/%{name}/.*\\.so$
#

# Set up a new macro to define MOC's 'mocp' executable
%global   exec   mocp

Name:    moc
Summary: Music on Console - Console audio player for Linux/UNIX
Version: 2.5.2
Release: 1%{?dist}
License: GPLv2+ and GPLv3+
URL:     http://moc.daper.net
Source0: http://ftp.daper.net/pub/soft/moc/stable/moc-%{version}.tar.bz2

BuildRequires: pkgconfig(ncurses)
BuildRequires: pkgconfig(alsa) 
BuildRequires: pkgconfig(jack)
BuildRequires: pkgconfig(libcurl) 
BuildRequires: pkgconfig(samplerate) 
BuildRequires: pkgconfig(taglib) 
BuildRequires: pkgconfig(speex) 
BuildRequires: pkgconfig(id3tag) 
BuildRequires: pkgconfig(vorbis) 
BuildRequires: pkgconfig(flac) 
BuildRequires: pkgconfig(zlib) 
BuildRequires: pkgconfig(sndfile) 
BuildRequires: pkgconfig(libmodplug) 
BuildRequires: pkgconfig(libtimidity) 
BuildRequires: pkgconfig(wavpack) 
BuildRequires: libdb-devel 
BuildRequires: libtool-ltdl-devel 
BuildRequires: gettext-devel 
BuildRequires: pkgconfig(opus)
BuildRequires: libtool
BuildRequires: librcc-devel
BuildRequires: popt-devel
BuildRequires: ffmpeg-devel
BuildRequires: libmad-devel
BuildRequires: faad2-devel

Requires: ffmpeg

%description
MOC (music on console) is a console audio player for LINUX/UNIX designed to be
powerful and easy to use. You just need to select a file from some directory
using the menu similar to Midnight Commander, and MOC will start playing all
files in this directory beginning from the chosen file.

%prep
%setup -q -n moc-%{version}

%build
%configure --disable-static --disable-silent-rules --disable-rpath --with-rcc \
 --with-oss --with-alsa --with-jack --with-aac --with-mp3 \
 --with-musepack --with-vorbis --with-flac --with-wavpack \
 --with-sndfile --with-modplug --with-ffmpeg --with-speex \
 --with-samplerate --with-curl --disable-debug --without-magic \
 CPPFLAGS="-I%{_includedir}/libdb -fPIC"
 
%make_build

%install
%make_install
rm -rf $RPM_BUILD_ROOT%{_datadir}/doc
rm -f $RPM_BUILD_ROOT%_libdir/*.la
rm -f $RPM_BUILD_ROOT%_libdir/moc/decoder_plugins/*.la

%files
%doc README README_equalizer AUTHORS ChangeLog config.example keymap.example NEWS
%license COPYING
%{_bindir}/%{exec}
%{_datadir}/%{name}/
%{_mandir}/man1/%{exec}.*
%{_libdir}/%{name}/

%changelog
* Wed Nov 16 2016 Antonio Trande <sagitter@fedoraproject.org> - 2.5.2-1
- Update to 2.5.2

* Sun Sep 04 2016 Antonio Trande <sagitter@fedoraproject.org> - 2.5.1-4
- Filtering of private libraries
- Rebuild for ffmpeg 3.0.2

* Sun Jun 05 2016 Antonio Trande <sagitter@fedoraproject.org> - 2.5.1-3
- Rebuild for ffmpeg 2.8.7

* Mon May 16 2016 Antonio Trande <sagitter@fedoraproject.org> - 2.5.1-2
- Add faad2 dependencies

* Tue Apr 26 2016 Antonio Trande <sagitter@fedoraproject.org> - 2.5.1-1
- Update to 2.5.1

* Tue Sep 02 2014 Antonio Trande <sagitter@fedoraproject.org> 2.5.0-2
- Spec cleanups

* Sat Aug 30 2014 Antonio Trande <sagitter@fedoraproject.org> 2.5.0-1
- Update to release 2.5.0 (Consolidation)

* Thu Aug 07 2014 Sérgio Basto <sergio@serjux.com> - 2.5.0-0.16.beta2
- Rebuilt for ffmpeg-2.3
- Conditional builds for ARM

* Tue May 13 2014 Antonio Trande <sagitter@fedoraproject.org> 2.5.0-0.15.beta2
- New svn commit of MOC-2.5.0 pre-release (r2641)

* Sat Mar 29 2014 Sérgio Basto <sergio@serjux.com> 2.5.0-0.14.beta2
- Rebuilt for ffmpeg-2.2

* Thu Mar 20 2014 Antonio Trande <sagitter@fedoraproject.org> 2.5.0-0.13.beta2
- New svn commit of MOC-2.5.0 pre-release
- Fixed release increment number for the pre-releases

* Wed Feb 26 2014 Antonio Trande <sagitter@fedoraproject.org> 2.5.0-0.12.beta2
- Fix unstripped-binary-or-object warnings for ARM builds

* Wed Feb 05 2014 Antonio Trande <sagitter@fedoraproject.org> 2.5.0-0.11.beta2
- Update to 2.5.0-beta2
- Removed previous patches

* Tue Jun 18 2013 Antonio Trande <sagitter@fedoraproject.org> 2.5.0-0.10.beta1
- Added patchset to fix "Unsupported sample size!" error
  See http://moc.daper.net/node/862 for more details
- Added patch for 'sizeof' argument bug
- Added BR: Autoconf and Automake-1.13 (temporarily)
- 'configure.in' renaming

* Sat Jun 08 2013 Antonio Trande <sagitter@fedoraproject.org> 2.5.0-0.9.beta1
- Removed some explicit Requires (curl, jack-audio-connection-kit, ncurses, speex)

* Fri Jun 07 2013 Antonio Trande <sagitter@fedoraproject.org> 2.5.0-0.8.beta1
- Fixed Source0 line
- Package owns %%{_libdir}/%%{name} directory

* Mon May 20 2013 Antonio Trande <sagitter@fedoraproject.org> 2.5.0-0.7.beta1
- Dist tag changed to %%{?dist}

* Tue Apr 09 2013 Antonio Trande <sagitter@fedoraproject.org> 2.5.0-0.6.beta1
- Removed autoreconf task from %%build section

* Fri Apr 05 2013 Antonio Trande <sagitter@fedoraproject.org> 2.5.0-0.5.beta1
- Removed libRCC explicit require

* Sun Mar 03 2013 Antonio Trande <sagitter@fedoraproject.org> 2.5.0-0.4.beta1
- Removed DESTDIR from %%make_install
- Changed source link with a public one
- Set up a new macro to define MOC's 'mocp' executable
- Added %%{name} prefix to the patch

* Tue Dec 25 2012 Antonio Trande <sagitter@fedoraproject.org> 2.5.0-0.3.beta1
- Added librcc support (fixes encoding in broken mp3 tags)

* Mon Oct 22 2012 Antonio Trande <sagitter@fedoraproject.org> 2.5.0-0.2.beta1
- Added patch to fix FSF address

* Mon Oct 22 2012 Antonio Trande <sagitter@fedoraproject.org> 2.5.0-0.1.beta1
- 2.5.0-beta1
