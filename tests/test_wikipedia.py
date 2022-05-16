from hyper_pee import wikipedia


def test_random_page_uses_given_language(mock_requests_get):
    wikipedia.random_page(language="fr")
    args, _ = mock_requests_get.call_args
    assert "fr.wikipedia.org" in args[0]
