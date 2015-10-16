%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Summary:	Majongg game for KDE
Name:		kajongg
Version:	15.08.2
Release:	1
Epoch:		1
Group:		Graphical desktop/KDE
License:	GPLv2+ and LGPLv2+ and GFDL
Url:		http://www.kde.org/applications/games/kajongg/
Source0:	ftp://ftp.kde.org/pub/kde/%{stable}/applications/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	kdelibs-devel
BuildRequires:	python-kde4-devel
BuildRequires:	python-qt4-devel
BuildRequires:	python2-kde4
BuildRequires:	python2-twisted
BuildRequires:	python2-sip
BuildRequires:	pkgconfig(sqlite3)
Requires:	python2-kde4
Requires:	python2-twisted
Requires:	qt4-database-plugin-sqlite
Requires:	kmahjongglib
# kajongg needed ogg123 @ runtime
Requires:	vorbis-tools
BuildArch:	noarch

%description
Kajongg is the ancient Chinese board game for 4 players.

Kajongg can be used in two different ways: Scoring a manual game where you play
as always and use Kajongg for the computation of scores and for bookkeeping. Or
you can use Kajongg to play against any combination of other human players or
computer players.

%files
%{_kde_bindir}/kajongg
%{_kde_bindir}/kajonggserver
%{_kde_applicationsdir}/kajongg.desktop
%{_kde_appsdir}/kajongg
%{_kde_docdir}/HTML/en/kajongg
%{_kde_iconsdir}/hicolor/*/*/*kajongg*
%{_datadir}/appdata/kajongg.appdata.xml

#------------------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde4 -DPYTHON_EXECUTABLE=%{__python2} -DCMAKE_MINIMUM_REQUIRED_VERSION=2.6
%make

%install
%makeinstall_std -C build
