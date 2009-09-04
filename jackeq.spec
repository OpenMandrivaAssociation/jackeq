%define name	jackeq
%define version	0.4.1
%define release %mkrel 7

Name: 	 	%{name}
Summary: 	Live EQ console for JACK audio applications
Version: 	%{version}
Release: 	%{release}

Source:		http://prdownloads.sourceforge.net/jackeq/jackEQ-%{version}.tar.bz2
URL:		http://jackeq.sourceforge.net/
License:	GPL
Group:		Sound
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	pkgconfig 
BuildRequires:  libjack-devel 
BuildRequires:  libxml2-devel 
BuildRequires:  gtk+2-devel 
BuildRequires:  gettext
BuildRequires:  ladspa-devel
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
%setup -q -n jackEQ-%version

%build
%configure2_5x
%make
										
%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

#menu

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}.desktop << EOF
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

%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post
%update_menus
%endif
		
%if %mdkversion < 200900
%postun
%clean_menus
%endif

%files
%defattr(-,root,root)
%doc AUTHORS README TODO
%{_bindir}/%name
%{_datadir}/%name
%{_datadir}/applications/mandriva-%{name}.desktop

