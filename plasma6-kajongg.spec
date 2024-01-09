%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Summary:	Majongg game for KDE
Name:		plasma6-kajongg
Version:	24.01.85
Release:	1
Group:		Graphical desktop/KDE
License:	GPLv2+ and LGPLv2+ and GFDL
Url:		http://www.kde.org/applications/games/kajongg/
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/kajongg-%{version}.tar.xz
BuildRequires:	python-qt6-gui
BuildRequires:	python-twisted
BuildRequires:	pkgconfig(sqlite3)
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KMahjongglib6)
BuildRequires:	pkgconfig(python3)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6Gui)
BuildRequires:	cmake(Qt6Svg)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(KF6Config)
BuildRequires:	cmake(KF6DocTools)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6ConfigWidgets)
Requires:	python-twisted
Requires:	qt6-database-plugin-sqlite
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

%files -f kajongg.lang
%{_bindir}/kajongg
%{_bindir}/kajonggserver
%{_datadir}/applications/org.kde.kajongg.desktop
%{_datadir}/icons/hicolor/*/*/*kajongg*
%{_datadir}/kajongg
%{_datadir}/metainfo/org.kde.kajongg.appdata.xml

#------------------------------------------------------------------------------

%prep
%autosetup -p1 -n kajongg-%{version}
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang kajongg --with-html
