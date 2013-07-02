Summary:	Majongg game for KDE
Name:		kajongg
Epoch:		1
Version:	4.10.5
Release:	1
Group:		Graphical desktop/KDE
License:	GPLv2 and LGPLv2 and GFDL
Url:		http://www.kde.org/applications/games/kajongg/
Source:		ftp://ftp.kde.org/pub/kde/stable/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	kdelibs4-devel
BuildRequires:	python-kde4
BuildRequires:	python-qt4
BuildRequires:	python-twisted-core
BuildRequires:	pkgconfig(sqlite3)
Requires:	python-kde4
Requires:	python-twisted-core
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

#------------------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

%changelog
* Wed Jul 03 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.5-1
- New version 4.10.5

* Wed Jun 05 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.4-1
- New version 4.10.4

* Tue May 07 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.3-1
- New version 4.10.3

* Wed Apr 03 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.2-1
- New version 4.10.2

* Sat Mar 09 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.1-1
- New version 4.10.1

* Wed Feb 13 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.0-1
- Split from kdegames4 package
- Should be noarch package

