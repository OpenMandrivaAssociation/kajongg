%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Summary:	Majongg game for KDE
Name:		kajongg
Version:	17.04.2
Release:	1
Epoch:		1
Group:		Graphical desktop/KDE
License:	GPLv2+ and LGPLv2+ and GFDL
Url:		http://www.kde.org/applications/games/kajongg/
Source0:	http://download.kde.org/%{stable}/applications/%{version}/src/%{name}-%{version}.tar.xz
Patch0:		fix-i18n.patch
BuildRequires:	python-qt5-gui
BuildRequires:	python-twisted
BuildRequires:	pkgconfig(sqlite3)
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF5KMahjongglib)
BuildRequires:	pkgconfig(python3)
BuildRequires:	cmake(Qt5Core)
BuildRequires:	cmake(Qt5Gui)
BuildRequires:	cmake(Qt5Svg)
BuildRequires:	cmake(Qt5Widgets)
BuildRequires:	cmake(KF5Config)
BuildRequires:	cmake(KF5DocTools)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5ConfigWidgets)
Requires:	python-twisted
Requires:	qt5-database-plugin-sqlite
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

%files -f %{name}.lang
%{_datadir}/applications/org.kde.kajongg.desktop
%{_datadir}/icons/hicolor/*/*/*kajongg*
%{_datadir}/kajongg
%{_datadir}/metainfo/org.kde.kajongg.appdata.xml

#------------------------------------------------------------------------------

%prep
%setup -q
%apply_patches

# Workaround for kde#376303
export PYTHONDONTWRITEBYTECODE=1
export DESTDIR=%{buildroot}

%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang kajongg --with-html
