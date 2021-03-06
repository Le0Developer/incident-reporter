# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]


## [0.2.4]

### Added

- Devs commands for restricting access to the bot for certain guilds

## [0.2.3]

### Added

- Error handler for being on cooldown
- `partialoutage` alias for `partial-outage`
- `dev_update` command for pulling from git and restarting thte bot
- Command help to `statusincident`

### Fixed

- Fixed prometheus from logging non-error

### Changed

- Changed `create_gift` to `dev_gengift`


## [0.2.2]

### Added

- You can now create an incident for multiple system in statusembeds


## [0.2.1]

### Fixed

- Fixed a bug with the premium check


## [0.2.0]

### Added

- Premium subscription for helping with hosting costs
- Statusembeds


## [0.1.2]

### Added

- Added prometheus extension
- Added `in!timezone` command for changing the timezone of incidents

### Changed

- Changed to urlsafe base64 for error logs


## [0.1.1]

### Added

- Added timestamp to incident embed


## [0.1.0]

### Added

- First commit


[Unreleased]: https://github.com/Le0Developer/incident-reporter/compare/v0.2.4...HEAD
[0.2.4]: https://github.com/Le0Developer/incident-reporter/compare/v0.2.3...v0.2.4
[0.2.3]: https://github.com/Le0Developer/incident-reporter/compare/v0.2.2...v0.2.3
[0.2.2]: https://github.com/Le0Developer/incident-reporter/compare/v0.2.1...v0.2.2
[0.2.1]: https://github.com/Le0Developer/incident-reporter/compare/v0.2.0...v0.2.1
[0.2.0]: https://github.com/Le0Developer/incident-reporter/compare/v0.1.2...v0.2.0
[0.1.2]: https://github.com/Le0Developer/incident-reporter/compare/v0.1.1...v0.1.2
[0.1.1]: https://github.com/Le0Developer/incident-reporter/compare/v0.1.0...v0.1.1
[0.1.0]: https://github.com/Le0Developer/incident-reporter/releases/tag/v0.1.0
