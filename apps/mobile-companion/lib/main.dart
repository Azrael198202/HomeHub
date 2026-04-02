import 'package:flutter/material.dart';

void main() {
  runApp(const HomeHubMobileApp());
}

class HomeHubMobileApp extends StatelessWidget {
  const HomeHubMobileApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      title: 'HomeHub Companion',
      theme: ThemeData(
        colorScheme: ColorScheme.fromSeed(seedColor: const Color(0xFF2E8B7D)),
        useMaterial3: true,
      ),
      home: const CompanionHomePage(),
    );
  }
}

class CompanionHomePage extends StatelessWidget {
  const CompanionHomePage({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('HomeHub Companion'),
      ),
      body: ListView(
        padding: const EdgeInsets.all(20),
        children: const [
          _StatusCard(
            title: 'QR Pairing',
            detail: 'Scan the box QR code to attach this device.',
          ),
          _StatusCard(
            title: 'Voice Command',
            detail: 'Press and hold to send a spoken instruction to the box.',
          ),
          _StatusCard(
            title: 'Image + Text',
            detail: 'Forward bill screenshots, travel notes, and questions to HomeHub.',
          ),
        ],
      ),
    );
  }
}

class _StatusCard extends StatelessWidget {
  final String title;
  final String detail;

  const _StatusCard({
    required this.title,
    required this.detail,
  });

  @override
  Widget build(BuildContext context) {
    return Card(
      margin: const EdgeInsets.only(bottom: 16),
      child: Padding(
        padding: const EdgeInsets.all(16),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Text(title, style: Theme.of(context).textTheme.titleLarge),
            const SizedBox(height: 8),
            Text(detail),
          ],
        ),
      ),
    );
  }
}
