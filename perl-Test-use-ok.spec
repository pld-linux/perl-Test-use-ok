#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Test
%define	pnam	use-ok
Summary:	Test::use::ok - Alternative to Test::More::use_ok
Summary(pl.UTF-8):	Test::use::ok - alternatywa dla Test::More::use_ok
Name:		perl-Test-use-ok
Version:	0.01
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/A/AU/AUTRIJUS/Test-use-ok-0.01.tar.gz
# Source0-md5:	57b8f1698b14c7ddef3b35b29ac3326c
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
According to the Test::More documentation, it is recommended to run
use_ok() inside a BEGIN block, so functions are exported at
compile-time and prototypes are properly honored.

That is, instead of writing this:

    use_ok( 'Some::Module' );
    use_ok( 'Other::Module' );

One should write this:

    BEGIN { use_ok( 'Some::Module' ); }
    BEGIN { use_ok( 'Other::Module' ); }

However, people often either forget to add BEGIN, or mistakenly group
use_ok with other tests in a single BEGIN block, which can create
subtle differences in execution order.

With this module, simply change all use_ok in test scripts to use ok,
and they will be executed at BEGIN time. The explicit space after use
makes it clear that this is a single compile-time action.

%description -l pl.UTF-8
Zgodnie z dokumentacją Test::More, zaleca się wywoływanie use_ok()
wewnątrz bloku BEGIN, aby funkcje były eksportowane w czasie
kompilacji, a prototypy odpowiednio honorowane.

Czyli zamiast pisania tak:

    use_ok( 'Jakis::Modul' );
    use_ok( 'Inny::Modul' );

Powinno pisać się tak:

    BEGIN { use_ok( 'Jakis::Modul' ); }
    BEGIN { use_ok( 'Inny::Modul' ); }

Jednak ludzie często zapominają dodać BEGIN lub błędnie grupują use_ok
z innymi testami w pojedynczym bloku BEGIN, co może powodować subtelne
różnice w kolejności wykonywania.

Przy użyciu tego modułu wystarczy zmienić wszystkie use_ok w skryptach
testowych na use ok, i zostaną one wykonane w czasie BEGIN. Spacja po
use daje jasność, że jest to pojedyncza akcja w czasie kompilacji.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/Test/use
%{perl_vendorlib}/ok.pm
%{_mandir}/man3/*
