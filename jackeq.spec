%define	oname	jackEQ

Name:		jackeq
Summary:		Live EQ console for JACK audio applications
Version:		0.5.9
Release:		2
URL:		http://djcj.org/%{name}/
License:		GPLv2+
Group:		Sound
Source0:		http://djcj.org/%{name}/code/%{oname}-%{version}.tar.bz2
Patch0:		jackeq-0.5.9-fix-format-string.patch
BuildRequires:	pkgconfig
BuildRequires:	jackit-devel >= 0.50.0
BuildRequires:	libxml2-devel >= 2.0
BuildRequires:	gtk+2-devel
BuildRequires:	gettext
BuildRequires:	ladspa-devel
Requires:	swh-plugins >= 0.4.2.20030819

%description
jackEQ is a tool for routing and manipulating audio from/to multiple
input/output sources. It runs in the JACK Audio Connection Kit, and uses
LADSPA for its backend DSP work, specifically the DJ EQ swh plugin created
by Steve Harris, one of jackEQ's main authors.
jackEQ is intended to provide an accessible method for tweaking the treble,
mid and bass of any JACK aware applications output. Designed specifically for
live performance, it is modelled on varous DJ mixing consoles which the main
author has used.


%prep
%setup -qn %{oname}-%{version}
%autopatch -p1


%build
export LIBS="-lm -lpthread -ljack -lxml2 -ldl"
%configure2_5x 
%make


%install
%makeinstall_std

#menu
mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Name=JackEQ
Comment=%{summary}
Exec=%{_bindir}/%{name}
Icon=sound_section
Terminal=false
Type=Application
Categories=AudioVideo;Mixer;
Encoding=UTF-8
EOF


%files
%doc AUTHORS README TODO
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop



%changelog
* Fri Nov 02 2012 Giovanni Mariani <mc2374@mclink.it> 0.5.9-1
- New release 0.5.9
- Dropped BuildRoot, %%mkrel, %%defattr and %%clean section
- Dropped support for ancient distro releases
- Updated URL and License tags
- Fixed BReq for jackit devel package
- Added P0 to fix build errors with Werror-format-string
- Fixed linking with libdl
- Removed uses of the deprecated "$RPM_BUILD_ROOT" macro

* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 0.4.1-8mdv2011.0
+ Revision: 619699
- the mass rebuild of 2010.0 packages

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 0.4.1-7mdv2010.0
+ Revision: 429581
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.4.1-6mdv2009.0
+ Revision: 247327
- rebuild

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Thu Feb 14 2008 Thierry Vignaud <tv@mandriva.org> 0.4.1-4mdv2008.1
+ Revision: 167923
- fix no-buildroot-tag
- kill re-definition of %%buildroot on Pixel's request

* Sat Sep 08 2007 Emmanuel Andry <eandry@mandriva.org> 0.4.1-4mdv2008.0
+ Revision: 82451
- drop old menu
- Import jackeq



* Sun Sep 03 2006 Emmanuel Andry <eandry@mandriva.org> 0.4.1-3mdv2007.0
- xdg menu

* Fri May 05 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.4.1-2mdk
- Fix BuildRequires

* Thu May 04 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.4.1-1mdk
- New release 0.4.1
- use mkrel

* Wed Dec 29 2004 Austin Acton <austin@mandrake.org> 0.4.0-1mdk
- 0.4.0
- source URL
- confiugre 2.5

* Thu Nov 13 2003 Austin Acton <aacton@yorku.ca> 0.3.6-1mdk
- 0.3.6

* Sat Oct 11 2003 Austin Acton <aacton@yorku.ca> 0.3.3-1mdk
- 0.3.3

* Tue Oct 7 2003 Austin Acton <aacton@yorku.ca> 0.3.2-0.20031007.1mdk
- initial package
