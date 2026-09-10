
-- Data for player
INSERT INTO player (id_player, username, password, elo, email, pokemon_fan, access_token) VALUES (2, 'a', '961b6dd3ede3cb8ecbaacbd68de040cd78eb2ed5889130cceb4c49268ea4d506', 1200, 'a@ensai.fr', True, NULL);
INSERT INTO player (id_player, username, password, elo, email, pokemon_fan, access_token) VALUES (1, 'admin', '69371091eb0f9aec7e61b7421cf3044529167e979cd975201909eb8ae33887ba', NULL, 'admin@project.io', NULL, NULL);
INSERT INTO player (id_player, username, password, elo, email, pokemon_fan, access_token) VALUES (4, 'batricia', 'e99bf7ce2b5216ff9811d3518cfe4499ddb9cb398e01600046a8f556d3e0b358', 1500, 'bat@project.io', False, NULL);
INSERT INTO player (id_player, username, password, elo, email, pokemon_fan, access_token) VALUES (6, 'gilbert', '968356512a7c3c61686eaabe4e6bce327a4f3937bcc7dd7f97498b505a1d4119', 1100, 'gilbert@project.io', False, NULL);
INSERT INTO player (id_player, username, password, elo, email, pokemon_fan, access_token) VALUES (7, 'junior', '9d6ecb35e514a49d7ea1df9dca7ac74d05fae531081f5860153697957fa66bc4', 1200, 'junior@project.io', True, NULL);
INSERT INTO player (id_player, username, password, elo, email, pokemon_fan, access_token) VALUES (3, 'maurice', '2b9ff2caf3872dda673847ec75ff6ae0968fc0c24a2b7e4bb6aeb21288ba462e', 1000, 'maurice@ensai.fr', True, NULL);
INSERT INTO player (id_player, username, password, elo, email, pokemon_fan, access_token) VALUES (5, 'miguel', 'c3b9d2196e24f68d35091ecc3615bb8b3cd12b127e06e86b64e533f9844d6c2e', 1300, 'miguel@project.io', True, NULL);

-- Data for game
INSERT INTO game (id_game, id_player1, id_player2, game_mode, id_winner, detail, timestamp) VALUES (1, 1, 2, 'coinflip', 1, 'Gilbert chose heads, result was heads', 2026-09-10 11:34:34.076390);
INSERT INTO game (id_game, id_player1, id_player2, game_mode, id_winner, detail, timestamp) VALUES (2, 3, 4, 'dice', 3, 'Maurice rolled 5, Batricia rolled 2', 2026-09-10 11:34:34.076390);
INSERT INTO game (id_game, id_player1, id_player2, game_mode, id_winner, detail, timestamp) VALUES (3, 3, 4, 'dice', NULL, 'Maurice rolled 4, Batricia rolled 4', 2026-09-10 11:34:34.076390);
INSERT INTO game (id_game, id_player1, id_player2, game_mode, id_winner, detail, timestamp) VALUES (4, 4, 3, 'dice', 4, 'Batricia rolled 2, Maurice rolled 1', 2026-09-10 11:34:34.076390);
INSERT INTO game (id_game, id_player1, id_player2, game_mode, id_winner, detail, timestamp) VALUES (5, 3, 4, 'coinflip', 4, 'Maurice chose heads, result was tails', 2026-09-10 11:34:34.076390);
INSERT INTO game (id_game, id_player1, id_player2, game_mode, id_winner, detail, timestamp) VALUES (6, 2, 4, 'monopoly', 2, '', 2026-09-10 12:58:32.159063);
