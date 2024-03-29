# * insta and ref-cast are not packaged
%bcond_with check
%global debug_package %{nil}

%global crate syn

Name:           rust-%{crate}
Version:        2.0.39
Release:        1
Summary:        Parser for Rust source code

# Upstream license specification: MIT OR Apache-2.0
License:        MIT or ASL 2.0
URL:            https://crates.io/crates/syn
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Parser for Rust source code.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE-MIT LICENSE-APACHE
%doc README.md
%{cargo_registry}/%{crate}-%{version_no_tilde}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+clone-impls-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+clone-impls-devel %{_description}

This package contains library source intended for building other packages
which use "clone-impls" feature of "%{crate}" crate.

%files       -n %{name}+clone-impls-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+derive-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+derive-devel %{_description}

This package contains library source intended for building other packages
which use "derive" feature of "%{crate}" crate.

%files       -n %{name}+derive-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+extra-traits-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+extra-traits-devel %{_description}

This package contains library source intended for building other packages
which use "extra-traits" feature of "%{crate}" crate.

%files       -n %{name}+extra-traits-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+fold-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+fold-devel %{_description}

This package contains library source intended for building other packages
which use "fold" feature of "%{crate}" crate.

%files       -n %{name}+fold-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+full-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+full-devel %{_description}

This package contains library source intended for building other packages
which use "full" feature of "%{crate}" crate.

%files       -n %{name}+full-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+parsing-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+parsing-devel %{_description}

This package contains library source intended for building other packages
which use "parsing" feature of "%{crate}" crate.

%files       -n %{name}+parsing-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+printing-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+printing-devel %{_description}

This package contains library source intended for building other packages
which use "printing" feature of "%{crate}" crate.

%files       -n %{name}+printing-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+proc-macro-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+proc-macro-devel %{_description}

This package contains library source intended for building other packages
which use "proc-macro" feature of "%{crate}" crate.

%files       -n %{name}+proc-macro-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+quote-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+quote-devel %{_description}

This package contains library source intended for building other packages
which use "quote" feature of "%{crate}" crate.

%files       -n %{name}+quote-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+visit-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+visit-devel %{_description}

This package contains library source intended for building other packages
which use "visit" feature of "%{crate}" crate.

%files       -n %{name}+visit-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+visit-mut-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+visit-mut-devel %{_description}

This package contains library source intended for building other packages
which use "visit-mut" feature of "%{crate}" crate.

%files       -n %{name}+visit-mut-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif
