%bcond_without	xmms	# disable xmms
%define		_decoration 	nvidia
Summary:	Kwin decoration - %{_decoration}
Summary(pl):	Dekoracja kwin - %{_decoration}
Name:		kde-decoration-%{_decoration}
Version:	1.0a
Release:	1
License:	LGPL
Group:		Themes
Source0:	%{_decoration}-%{version}-3.2.0.tar.bz2
# Source0-md5:	081e5072cb21e344e9fe3cb5c5a1c2b3
URL:		http://www.kde-look.org/content/show.php?content=12330
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	qt-devel >= 3.0.5
BuildRequires:	kdelibs-devel
#BuildRequires:	unsermake
%if %{with xmms}
BuildRequires:  xmms-devel
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
%{_decoration} kwin decoration.

%description -l pl
Dekoracja kwin %{_decoration}.

%package -n xmms-skin-%{_decoration}
Summary:        An xmms skin %{_decoration} theme
Summary(pl):    Sk�rka dla XMMS-a z motywu %{_decoration}
Group:          Themes
Requires:       xmms

%description -n xmms-skin-%{_decoration}
An xmms skin %{_decoration} theme.

%description -n xmms-skin-%{_decoration} -l pl
Sk�rka dla XMMS-a z motywu %{_decoration}.

%package -n kde-colorscheme-%{_decoration}
Summary:        Color scheme for KDE style - %{_decoration}
Summary(pl):    Schemat kolor�w do stylu KDE - %{_decoration}
Group:          Themes
Requires:       kdebase-core

%description -n kde-colorscheme-%{_decoration}
Color scheme for KDE style - %{_decoration}.

%description -n kde-colorscheme-%{_decoration} -l pl
Schemat kolor�w do stylu KDE - %{_decoration}.

%prep
%setup -q -n %{_decoration}-%{version}-3.2.0

%build
kde_htmldir="%{_kdedocdir}"; export kde_htmldir
kde_icondir="%{_iconsdir}"; export kde_icondir
cp -f /usr/share/automake/config.sub admin
##export UNSERMAKE=/usr/share/unsermake/unsermake
##%{__make} -f Makefile.cvs

%configure \
	--with-qt-libraries=%{_libdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

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
