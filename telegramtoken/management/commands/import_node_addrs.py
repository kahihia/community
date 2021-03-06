# -*- coding: utf-8 -*-
from django.core.management import BaseCommand
from django.contrib.auth.models import User
from telegramtoken.models import WalletID
from telegramtoken.utils import get_client


class Command(BaseCommand):

    def handle(self, *args, **options):
        client = get_client()

        user_obj = User.objects.get(username='demo')
        addrs = client.getaddresses()
        for addr in addrs:
            print('Import WalletID:', addr)
            wid, created = WalletID.objects.get_or_create(
                owner=user_obj,
                address=addr,
                memo='Demo User Wallet'
            )
            if created:
                print('Imported WalletID:', wid)
            else:
                print(wid, 'already exists.')
