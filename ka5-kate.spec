%define		kdeappsver	18.12.1
%define		qtver		5.9.0
%define		kaname		kate

Summary:	K Desktop Environment - Advanced Text Editor
Summary(pl.UTF-8):	K Desktop Environment -  Zaawansowany edytor tekstu
Name:		ka5-%{kaname}
Version:	18.12.1
Release:	1
License:	GPL
Group:		X11/Applications/Editors
Source0:	http://download.kde.org/stable/applications/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	9d387cf41ca11487097a2821265ed9f4
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel
BuildRequires:	Qt5DBus-devel
BuildRequires:	Qt5Gui-devel >= 5.11.1
BuildRequires:	Qt5Sql-devel
BuildRequires:	Qt5Test-devel >= 5.4.0
BuildRequires:	Qt5Widgets-devel
BuildRequires:	gettext-devel
BuildRequires:	kf5-extra-cmake-modules >= 5.53.0
BuildRequires:	kf5-kconfig-devel >= 5.40.0
BuildRequires:	kf5-kcrash-devel >= 5.40.0
BuildRequires:	kf5-kdbusaddons-devel
BuildRequires:	kf5-kguiaddons-devel >= 5.40.0
BuildRequires:	kf5-ki18n-devel >= 5.40.0
BuildRequires:	kf5-kiconthemes-devel >= 5.40.0
BuildRequires:	kf5-kio-devel >= 5.40.0
BuildRequires:	kf5-kjobwidgets-devel >= 5.40.0
BuildRequires:	kf5-knewstuff-devel >= 5.40.0
BuildRequires:	kf5-kparts-devel >= 5.53.0
BuildRequires:	kf5-ktexteditor-devel >= 5.40.0
BuildRequires:	kf5-kwindowsystem-devel >= 5.40.0
BuildRequires:	kf5-kxmlgui-devel >= 5.40.0
BuildRequires:	ninja
BuildRequires:	shared-mime-info
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KDE advanced text editor featuring among others:
- fast opening/editing of files even the big ones (opens a 50MB file
  in a few seconds)
- powerful syntaxhighlighting engine, extensible via XML files
- Code Folding capabilities for C++, C, PHP and more
- Dynamic Word Wrap - long lines are wrapped at the window border on
  the fly for better overview
- multiple views allows you to view more instances of the same
  document and/or more documents at one time
- support for different encodings globally and at write time
- built in dockable terminal emulation
- sidebars with a list of open documents, a directory viewer with a
  directory chooser, a filter chooser and more
- a plugin interface to allow third party plugins
- a "Filter" command allows you to run selected text through a shell
  command

KWrite is a simple texteditor, with syntaxhighlighting, codefolding,
dynamic word wrap and more, it's the lightweight version of Kate,
providing more speed for minor tasks.

%description -l pl.UTF-8
Kate (KDE advanced text editor) to zaawansowany edytor tekstu KDE o
możliwościach obejmujących m.in.:
- szybkie otwieranie i edycję nawet dużych plików (otwiera plik 50MB w
  parę sekund)
- potężny silnik podświetlania składni, rozszerzalny za pomocą plików
  XML
- możliwość zwijania kodu dla C++, C, PHP i innych języków
- dynamiczne zawijanie wierszy - długie linie są zawijane na granicy
  okna w locie dla lepszej widoczności
- wiele widoków pozwalających oglądać więcej instancji tego samego
  dokumentu i/lub więcej dokumentów w tym samym czasie
- obsługę różnych kodowań globalnie i w czasie zapisu
- wbudowaną emulację dokowalnego terminala
- paski z listą otwartych dokumentów, przeglądarkę katalogów z
  możliwością wybierania katalogu i filtrów
- interfejs wtyczek obsługujący zewnętrzne wtyczki
- polecenie "Filtr" pozwalające przepuszczać zaznaczony tekst przez
  polecenie powłoki

KWrite to prosty edytor tekstu z podświetlaniem składni, zwijaniem
kodu, dynamicznym zawijaniem wierszy itp. Jest lżejszą wersją Kate,
szybszą dla mniejszych zadań.

%package devel
Summary:	kate development files
Summary(pl.UTF-8):	Pliki dla programistów kate
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Obsoletes:	kate-devel <= 4.8.0

%description devel
kate development files.

%description devel -l pl.UTF-8
Pliki dla programistów kate.

%prep
%setup -q -n %{kaname}-%{version}

%build
install -d build
cd build
%cmake \
	-G Ninja \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%ninja_build

%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{kaname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kate
%attr(755,root,root) %{_bindir}/kwrite
%{_libdir}/qt5/plugins/ktexteditor/katebacktracebrowserplugin.so
%{_libdir}/qt5/plugins/ktexteditor/katebuildplugin.so
%{_libdir}/qt5/plugins/ktexteditor/katecloseexceptplugin.so
%{_libdir}/qt5/plugins/ktexteditor/katectagsplugin.so
%{_libdir}/qt5/plugins/ktexteditor/katefilebrowserplugin.so
%{_libdir}/qt5/plugins/ktexteditor/katefiletreeplugin.so
%{_libdir}/qt5/plugins/ktexteditor/kategdbplugin.so
%{_libdir}/qt5/plugins/ktexteditor/katekonsoleplugin.so
%{_libdir}/qt5/plugins/ktexteditor/kateopenheaderplugin.so
%{_libdir}/qt5/plugins/ktexteditor/kateprojectplugin.so
%{_libdir}/qt5/plugins/ktexteditor/katereplicodeplugin.so
%{_libdir}/qt5/plugins/ktexteditor/katesearchplugin.so
%{_libdir}/qt5/plugins/ktexteditor/katesnippetsplugin.so
%{_libdir}/qt5/plugins/ktexteditor/katesqlplugin.so
%{_libdir}/qt5/plugins/ktexteditor/katesymbolviewerplugin.so
%{_libdir}/qt5/plugins/ktexteditor/katexmlcheckplugin.so
%{_libdir}/qt5/plugins/ktexteditor/katexmltoolsplugin.so
%{_libdir}/qt5/plugins/ktexteditor/kterustcompletionplugin.so
%{_libdir}/qt5/plugins/ktexteditor/ktexteditor_lumen.so
%{_libdir}/qt5/plugins/ktexteditor/tabswitcherplugin.so
%{_libdir}/qt5/plugins/ktexteditor/textfilterplugin.so
%{_libdir}/qt5/plugins/ktexteditor/ktexteditorpreviewplugin.so
%{_libdir}/qt5/plugins/plasma/dataengine/plasma_engine_katesessions.so
%{_desktopdir}/org.kde.kate.desktop
%{_desktopdir}/org.kde.kwrite.desktop
%{_iconsdir}/hicolor/128x128/apps/kate.png
%{_iconsdir}/hicolor/128x128/apps/kwrite.png
%{_iconsdir}/hicolor/16x16/apps/kate.png
%{_iconsdir}/hicolor/16x16/apps/kwrite.png
%{_iconsdir}/hicolor/22x22/apps/kate.png
%{_iconsdir}/hicolor/22x22/apps/kwrite.png
%{_iconsdir}/hicolor/32x32/apps/kate.png
%{_iconsdir}/hicolor/32x32/apps/kwrite.png
%{_iconsdir}/hicolor/48x48/apps/kate.png
%{_iconsdir}/hicolor/48x48/apps/kwrite.png
%{_iconsdir}/hicolor/64x64/apps/kate.png
%{_iconsdir}/hicolor/64x64/apps/kwrite.png
%{_iconsdir}/hicolor/scalable/apps/kate.svgz
%{_iconsdir}/hicolor/scalable/apps/kwrite.svgz
%dir %{_datadir}/kateproject
%{_datadir}/kateproject/kateproject.example
%dir %{_datadir}/katexmltools
%{_datadir}/katexmltools/html4-loose.dtd.xml
%{_datadir}/katexmltools/html4-strict.dtd.xml
%{_datadir}/katexmltools/kcfg.dtd.xml
%{_datadir}/katexmltools/kde-docbook.dtd.xml
%{_datadir}/katexmltools/kpartgui.dtd.xml
%{_datadir}/katexmltools/language.dtd.xml
%{_datadir}/katexmltools/simplify_dtd.xsl
%{_datadir}/katexmltools/testcases.xml
%{_datadir}/katexmltools/xhtml1-frameset.dtd.xml
%{_datadir}/katexmltools/xhtml1-strict.dtd.xml
%{_datadir}/katexmltools/xhtml1-transitional.dtd.xml
%{_datadir}/katexmltools/xslt-1.0.dtd.xml
%{_datadir}/kservices5/plasma-applet-org.kde.plasma.katesessions.desktop
%{_datadir}/kservices5/plasma-dataengine-katesessions.desktop
%{_mandir}/ca/man1/kate.1*
%{_mandir}/de/man1/kate.1*
%{_mandir}/es/man1/kate.1*
%{_mandir}/it/man1/kate.1*
%{_mandir}/man1/kate.1*
%{_mandir}/nl/man1/kate.1*
%{_mandir}/pt/man1/kate.1*
%{_mandir}/pt_BR/man1/kate.1*
%{_mandir}/sv/man1/kate.1*
%{_mandir}/uk/man1/kate.1*
%{_datadir}/metainfo/org.kde.kate.appdata.xml
%{_datadir}/metainfo/org.kde.kwrite.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.katesessions.appdata.xml
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.katesessions
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.katesessions/contents
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.katesessions/contents/ui
%{_datadir}/plasma/plasmoids/org.kde.plasma.katesessions/contents/ui/KateSessionsItemDelegate.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.katesessions/contents/ui/Menu.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.katesessions/contents/ui/katesessions.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.katesessions/metadata.desktop
%{_datadir}/plasma/plasmoids/org.kde.plasma.katesessions/metadata.json
%{_datadir}/plasma/services/org.kde.plasma.katesessions.operations
