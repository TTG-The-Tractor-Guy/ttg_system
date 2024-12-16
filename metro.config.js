const path = require('path');

module.exports = {
  resolver: {
    extraNodeModules: {
      shared: path.resolve(__dirname, '../../shared'),
    },
  },
  watchFolders: [path.resolve(__dirname, '../../shared')],
};
