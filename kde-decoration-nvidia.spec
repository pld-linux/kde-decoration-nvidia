#
# Conditional build:
%bcond_without	xmms	# disable xmms-skin
#
%define		_decoration 	nvidia
#
Summary:	Kwin decoration - %{_decoration}
Summary(pl.UTF-8):	Dekoracja kwin - %{_decoration}
Name:		kde-decoration-%{_decoration}
Version:	1.0b
Release:	1
License:	LGPL
Group:		Themes
Source0:	%{_decoration}-%{version}-3.2.0.tar.bz2
# Source0-md5:	556a523933a1094ffa971d928551fd1b
Patch0:		%{_decoration}-unsermake.patch
URL:		http://www.kde-look.org/content/show.php?content=12330
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	kdebase-devel >= 9:3.2.0
BuildRequires:	kdebase-desktop-libs >= 9:3.2.0
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRequires:	unsermake
Requires:	kdebase-desktop-libs >= 9:3.2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A clone of the nvidia Windows XP decoration. It features concave
window title alongside with rounded window corners.

%description -l pl.UTF-8
Klon dekoracji nvidia z Windows XP. Oferuje między innymi wklęsłe pole
z tytułem okna oraz zaokrąglone brzegi okna.

%package -n xmms-skin-%{_decoration}
Summary:	An XMMS skin %{_decoration} theme
Summary(pl.UTF-8):	Skórka dla XMMS-a z motywu %{_decoration}
Group:		Themes
Requires:	xmms

# These could use better usability but i have no xmms.
%description -n xmms-skin-%{_decoration}
An XMMS skin %{_decoration} theme.

%description -n xmms-skin-%{_decoration} -l pl.UTF-8
Skórka dla XMMS-a z motywu %{_decoration}.

%package -n kde-colorscheme-%{_decoration}
Summary:	Color scheme for KDE style - %{_decoration}
Summary(pl.UTF-8):	Schemat kolorów do stylu KDE - %{_decoration}
Group:		Themes
Requires:	kdebase-core

%description -n kde-colorscheme-%{_decoration}
A grey colorscheme with lime link and selection background.

%description -n kde-colorscheme-%{_decoration} -l pl.UTF-8
Szary schemat kolorów z odnośnikami i tłem zaznaczenia w kolorze
limonki.

%prep
%setup -q -n %{_decoration}-%{version}-3.2.0
%patch0 -p1

%build
cp -f /usr/share/automake/config.sub admin
export UNSERMAKE=/usr/share/unsermake/unsermake
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
