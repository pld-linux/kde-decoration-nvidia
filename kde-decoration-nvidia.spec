%bcond_without	xmms	# disable xmms
%bcond_with	kde	# use kde logo instead of nvidia one

%define		_decoration 	nvidia
Summary:	Kwin decoration - %{_decoration}
Summary(pl):	Dekoracja kwin - %{_decoration}
Name:		kde-decoration-%{_decoration}
Version:	1.0a
Release:	3
License:	LGPL
Group:		Themes
Source0:	%{_decoration}-%{version}-3.2.0.tar.bz2
# Source0-md5:	081e5072cb21e344e9fe3cb5c5a1c2b3
Patch0:		%{_decoration}-unsermake.patch
URL:		http://www.kde-look.org/content/show.php?content=12330
BuildRequires:	autoconf
BuildRequires:	unsermake
BuildRequires:	automake
BuildRequires:	kdelibs-devel >= 9:3.2.0
BuildRequires:	kdebase-desktop-libs >= 9:3.2.0
Requires:	kdebase-desktop-libs >= 9:3.2.0
%if %{with xmms}
BuildRequires:	xmms-devel
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A clone of the nvidia Windows XP decoration. It features concave
window title alongside with rounded window corners.

%description -l pl
Klon dekoracji nvidia z Windows XP. Oferuje miêdzy innymi wklês³e pole
z tytu³em okna oraz zaokr±glone brzegi okna.

%package -n xmms-skin-%{_decoration}
Summary:	An xmms skin %{_decoration} theme
Summary(pl):	Skórka dla XMMS-a z motywu %{_decoration}
Group:		Themes
Requires:	xmms

# These could use better usability but i have no xmms.
%description -n xmms-skin-%{_decoration}
An xmms skin %{_decoration} theme.

%description -n xmms-skin-%{_decoration} -l pl
Skórka dla XMMS-a z motywu %{_decoration}.

%package -n kde-colorscheme-%{_decoration}
Summary:	Color scheme for KDE style - %{_decoration}
Summary(pl):	Schemat kolorów do stylu KDE - %{_decoration}
Group:		Themes
Requires:	kdebase-core

%description -n kde-colorscheme-%{_decoration}
A grey colorscheme with lime link and selection background.

%description -n kde-colorscheme-%{_decoration} -l pl
Szary schemat kolorów z odno¶nikami i t³em zaznaczenia w kolorze
limonki.

%prep
%setup -q -n %{_decoration}-%{version}-3.2.0
%patch0 -p1

%build
%if %{with kde}
cp -rf kwin/pics/kde/* kwin/pics/
%endif

cp -f %{_datadir}/automake/config.sub admin
export UNSERMAKE=%{_datadir}/unsermake/unsermake
%{__make} -f Makefile.cvs

%configure \
	--with-qt-libraries=%{_libdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir="%{_kdedocdir}"

install -d $RPM_BUILD_ROOT%{_datadir}/apps/kdisplay/color-schemes
install other/nvidia.kcsrc $RPM_BUILD_ROOT%{_datadir}/apps/kdisplay/color-schemes

%if %{with xmms}
install -d $RPM_BUILD_ROOT%{xmms_datadir}/Skins
install other/SoftshapeAmp_Release_II_Color_1.wsz $RPM_BUILD_ROOT%{xmms_datadir}/Skins
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_libdir}/kde3/kwin*.la
%attr(755,root,root) %{_libdir}/kde3/kwin*.so
%{_datadir}/apps/kwin/*.desktop

%if %{with xmms}
%files -n xmms-skin-%{_decoration}
%defattr(644,root,root,755)
%{xmms_datadir}/Skins/*
%endif

%files -n kde-colorscheme-%{_decoration}
%defattr(644,root,root,755)
%{_datadir}/apps/kdisplay/color-schemes/*.kcsrc
